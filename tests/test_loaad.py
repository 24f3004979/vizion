from ingestion.ingest import *

data_path = "/home/madhavrimal/workspace/Projects/vizion/data.csv"

# This will raise an error during testing if any null slipped through


def test_load():
    df_cleaned = clean_load(data_path)
    assert df_cleaned.isna().sum().sum() == 0, "Null values are still present!"
