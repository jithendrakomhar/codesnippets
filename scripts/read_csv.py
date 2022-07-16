from cmath import nan
from numpy import NAN, NaN
import pandas as pd
import os


df = pd.read_csv('log/test.csv',header=0)

for idx in df.index:
    if (df.loc[idx,'id']):
        df.loc[idx,'name']

# for idx in df.index:

#     if(df.loc[idx,'id']<4):
#         df.loc[idx,'id']=100
#     else:
#         df.loc[idx,'id']=200

# df.to_csv('log/test.csv')
