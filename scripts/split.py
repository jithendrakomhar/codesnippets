from asyncore import write
from fileinput import filename
from operator import mod
import os 
import pandas as pd 

folder_name='C:/Users/jithe/OneDrive/Desktop/Latest/'
file_name= os.path.join(folder_name,'CACF_Analaysis_2022_07_updated_Jithu.xlsx')

df=pd.read_excel(file_name,header=0,sheet_name="Jithu")


df = df.assign(job_name=lambda row: [ col_value.rsplit("_",1)[0].replace(".item","") for col_value in   row['Job Name']])
df = df.assign(job_version=lambda row: [ col_value.rsplit("_",1)[1].replace(".item","") for col_value in   row['Job Name']])


df1 = df[['job_name','job_version']]

df2 =df.groupby('job_name', sort=False)['job_version'].max()

print(df2)