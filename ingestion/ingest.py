# Ingestion
"""
+ Load dataset into main Frame
+ Cleaning Null and outliers
"""

import pandas as pd
import numpy as np


def clean_load(file_path: str) -> pd.DataFrame:
    """
    Data loading pipeline
        + Read and Load
    """

    df = pd.read_csv(file_path)
    # columns leading and trailing information
    df.columns = df.columns.str.strip()
    # Sanitize with String object refrences
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()
            # making default Nan values
            df[col] = df[col].replace({"": np.nan, "nan": np.nan, "NaN": np.nan})
        converted_numeric = pd.to_numeric(df[col], errors="coerce")
        # BUG : Numeric Entries are not parsed properly for conversion
        print(converted_numeric)
    return df
