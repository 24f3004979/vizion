# Ingestion
"""
+ Load dataset into main Frame
+ Cleaning Null and outliers
"""

import pandas as pd
import numpy as np


def clean_load(file_path: str) -> pd.DataFrame:
    """
    Cleaning and Loading
    removing simple amboguious data elements for clean data"""

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

        # Converion based allotment data column
        if (converted_numeric.notna().sum()) > (len(df) * 0.5):
            df[col] = converted_numeric  # Making that column into numric converion
            df[col] = df[col].fillna(0).astype("Int64")
        elif df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown").astype(str)
        else:
            df[col] = df[col].fillna(0.0)
    return df


def generic_clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Data copy | Refrence conflicts
    df = df.copy()
    df = df.replace([None, "None", "none", "NaN", "null", "NULL"], np.nan)

    # standardise the numeric dataset for nullity
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        # rest as unknown values
        else:
            df[col] = df[col].fillna("Unknown").astype(str)
    return df
