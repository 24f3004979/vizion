# core/service/Data.py
import io, json
import pandas as pd
from core.schema.exceptions import WrongLocation

class DataModel:
    MAX_HISTORY = 20  # snapshots are full copies, so cap them

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.undo_stack: list[pd.DataFrame] = []
        self.redo_stack: list[pd.DataFrame] = []
        self.version = 0

    @classmethod
    def from_csv_bytes(cls, raw: bytes):
        return cls(pd.read_csv(io.BytesIO(raw)))

    # ---------- reading ----------
    def page(self, page: int, page_size: int):
        total = len(self.df)
        total_pages = max(1, -(-total // page_size))   # ceiling division
        page = min(max(1, page), total_pages)
        offset = (page - 1) * page_size
        chunk = self.df.iloc[offset: offset + page_size]

        return {
            "columns": [{"name": str(c), "dtype": str(t)} for c, t in self.df.dtypes.items()],
            # records -> [{col: value}], NaN becomes null, dates become ISO strings
            "rows": json.loads(chunk.to_json(orient="records", date_format="iso")),
            "offset": offset,
            "page": page,
            "page_size": page_size,
            "total_rows": total,
            "total_pages": total_pages,
            "version": self.version,
            "can_undo": bool(self.undo_stack),
            "can_redo": bool(self.redo_stack),
        }

    # ---------- history ----------
    def _checkpoint(self):
        """Call BEFORE every change: saves a snapshot so it can be undone."""
        self.undo_stack.append(self.df.copy())
        self.undo_stack = self.undo_stack[-self.MAX_HISTORY:]
        self.redo_stack.clear()          # a new edit kills the redo branch
        self.version += 1

    def undo(self):
        if not self.undo_stack:
            return
        self.redo_stack.append(self.df)
        self.df = self.undo_stack.pop()
        self.version += 1

    def redo(self):
        if not self.redo_stack:
            return
        self.undo_stack.append(self.df)
        self.df = self.redo_stack.pop()
        self.version += 1

    # ---------- editing ----------
    def edit_cell(self, row: int, column: str, value):
        if column not in self.df.columns:
            raise WrongLocation(f"No column named '{column}'")
        if not 0 <= row < len(self.df):
            raise WrongLocation(f"Row {row} is out of range")

        col_idx = self.df.columns.get_loc(column)
        dtype = self.df[column].dtype
        # convert "42" (text from the browser) to the column's real type
        value = pd.Series([value]).astype(dtype).iloc[0]   # raises ValueError if impossible

        self._checkpoint()
        self.df.iat[row, col_idx] = value
