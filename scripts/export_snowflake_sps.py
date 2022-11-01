import snowflake
import os 

schema_list_file=r"F:\Python\codesnippets\log\db_schema.txt"


def db_execute_query(database_name,schema_name):
    conn = snowflake.connector.connect(
                    user='QA_KOMHAR',
                    password='hI@oc9#jrO@T',
                    account='NEXT_PATHWAY_PARTNER.us-east-1',
                    warehouse='INFA_POC',
                    database=database_name,
                    schema=schema_name
                    )
    return conn

def get_schema_list(schema_list_file):
    f_schema_list=open(schema_list_file,'r')
    schema_list=f_schema_list.read().splitlines()
    return schema_list




def main():
   schema_list=get_schema_list(schema_list_file)
   for schema_name in schema_list:
     generate_sp_ddl(schema_name)


if __name__ == "__main__":
    main()