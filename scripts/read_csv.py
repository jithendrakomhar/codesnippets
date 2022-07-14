import pandas as pd
import os



df = pd.read_csv('./log/file_list.txt')

for line in df.items():
    print(line)