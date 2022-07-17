from cgi import test
import pandas as pd 

print("jithu")

class test_class:

    def __init__(self) -> None:
        print("********************")


    def join_two_dfs(self):

        df_emp=pd.read_csv('F:\Python\codesnippets\log\dept.csv',header=0)
        df_dept=pd.read_csv('log/dept.csv',header=0).drop('id',axis=1)


        df1=df_emp.merge(df_dept,on='deptno',how='left',suffixes=('_1','_2'))

        print(df1)


def main():
    test_obj = test_class()
    test_obj.join_two_dfs()

if __name__=="__main__":
    main()
