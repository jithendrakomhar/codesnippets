import snowflake.connector as snowflake
import os 

schema_list_file=r"F:\Python\codesnippets\log\db_schema.txt"


def db_connect():
    snf_conn = snowflake.connect(
                    user='QA_KOMHAR',
                    password='hI@oc9#jrO@T',
                    account='NEXT_PATHWAY_PARTNER.us-east-1',
                    warehouse='INFA_POC')
    return snf_conn

def get_schema_list(schema_list_file):
    f_schema_list=open(schema_list_file,'r')
    schema_list=f_schema_list.read().splitlines()
    return schema_list

def execute_sql():
    snf_conn=db_connect()
    schema_name='REPOSITORY'
    database_name='DB_AV_DEV_STG'
    query1 = '''SELECT PROCEDURE_NAME FROM INFORMATION_SCHEMA.PROCEDURES WHERE PROCEDURE_SCHEMA = %s AND PROCEDURE_CATALOG = %s;'''
    tuple1 = (schema_name, database_name)
    cur = snf_conn.cursor()
    cur.execute('use db_av_dev_stg')
    cur.execute(query1, tuple1)
    sp = cur.fetchall()

    for sp_name in sp:
        print(sp_name)



def main():
   schema_list=get_schema_list(schema_list_file)
   for schema_name in schema_list:
     execute_sql()


if __name__ == "__main__":
    main()