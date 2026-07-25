'''
Type Inference unit
dataset -> type inference about each column

Input : Dataset.csv

Output : List of types infered about dataset

Execution Steps
1. Iterate for all columns
2. Infer their type with the iteration
3. report the type
'''
import pandas as pd 
import pandas.api.types as ptypes

def dtype_inspection(df, col):
    if ptypes.is_numeric_dtype(df[col]):
        if ptypes.is_integer_dtype(df[col]):
            return "integer"
        elif ptypes.is_float_dtype(df[col]):
            return "float"
    if ptypes.is_bool_dtype(df[col]):
        return "bool"
    if ptypes.is_categorical_dtype(df[col]):
        return "categorical"
    else:
        return "typ-not-detected"

df = pd.read_csv('data.csv')
print(dtype_inspection(df,'S.no' ))
