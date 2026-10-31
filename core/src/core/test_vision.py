# testing core functions
import pandas as pd

from core.utils import *

testing_path = '/home/madhav/workstation/Lab/experiment/data/titatic-dataset.csv'

def test_identifier():
    df = pd.read_csv(testing_path)
    ident = fetch_identifier_column(df)
    print(f'Identifier columns : {ident}')
    assert type(ident) == list