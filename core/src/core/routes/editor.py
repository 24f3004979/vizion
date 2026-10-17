# editor_route.py
from typing import Any
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from pydantic import BaseModel
from core.service.Data import DataModel
from core.schema.exceptions import WrongLocation

editor_route = APIRouter(prefix='/editor')

# single-user tool, so one dataset held in memory is enough
state: dict[str, DataModel | None] = {"model": None}

def model() -> DataModel:
    if state["model"] is None:
        raise HTTPException(404, "No dataset loaded yet")
    return state["model"]

class CellEdit(BaseModel):
    row: int
    column: str
    value: Any = None

@editor_route.post('/upload')
async def upload(file: UploadFile = File(...)):
    try:
        state["model"] = DataModel.from_csv_bytes(await file.read())
    except Exception as e:
        raise HTTPException(400, f"Could not read CSV: {e}")
    return state["model"].page(1, 50)

@editor_route.get('/data')
def get_data(page: int = Query(1, ge=1), page_size: int = Query(50, ge=1, le=500)):
    return model().page(page, page_size)

@editor_route.patch('/cell')
def edit_cell(body: CellEdit):
    try:
        model().edit_cell(body.row, body.column, body.value)
    except WrongLocation as e:
        raise HTTPException(404, str(e))
    except (ValueError, TypeError) as e:
        raise HTTPException(422, f"Value doesn't fit this column: {e}")
    return {"version": model().version}

@editor_route.post('/undo')
def undo():
    model().undo()
    return {"version": model().version}

@editor_route.post('/redo')
def redo():
    model().redo()
    return {"version": model().version}
