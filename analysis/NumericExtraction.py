"""
Making simple numerical extraction logic with dataset

Main Data loading module
            |
    Numerical extraction pipeline
    |
Visualization pipeline Engine for visuals & insights
"""

import numpy as np
import pandas as pd

agri_data = pd.read_csv("/home/madhavrimal/workspace/Projects/vizion/patterns.csv")

print(agri_data.head())
print("_" * 200)
print(f"Data overview : {agri_data.head()}")
