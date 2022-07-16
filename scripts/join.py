import pandas as pd 

df_emp=pd.read_csv('F:\Python\codesnippets\log\dept.csv',header=0)
df_dept=pd.read_csv('log/dept.csv',header=0).drop('id',axis=1)


df1=df_emp.merge(df_dept,on='deptno',how='left',suffixes=('_1','_2'))

print(df1)