from operator import index
import pandas as pd 

df=pd.read_excel('C:/Users/jithe/OneDrive/Desktop/Latest/CACF_Analaysis_2021-10_updated.xlsx',header=0,sheet_name="Job Raw Uniq")


gkk=df.groupby(['Spark'])
print(gkk.count('Status'))