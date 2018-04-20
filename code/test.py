import os
import pandas as pd
df = pd.read_csv('../data/1.csv')
df1 = pd.read_csv('../data/2.csv')
df1.to_csv('../data/1.csv' ,index=False)