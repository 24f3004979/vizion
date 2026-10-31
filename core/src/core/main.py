from rich import print
import pandas as pd
import sklearn

from core.utils import *


def ignite(path):
    df = pd.read_csv(path) # Data frame loaded

    idents = fetch_identifier_column(df)
    if idents is not None:
        drop(df, idents) # Droping identifiers
    
    numerical_columns = fetch_numerics(df)
    categorical_columns = fetch_categorical(df)

    encoding_handle(df) # Encoding handle



def main():
    print('--- [yellow] VIZION EDA TOOL [/yellow] ---')
    path = input("Enter path of your dataset :")
    ignite(path)
