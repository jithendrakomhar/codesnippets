import snowflake.connector as snowflake

schema_name='REPOSITORY'
database_name='DB_AV_DEV_STG'

conn = snowflake.Connect(
                    user='QA_KOMHAR',
                    password='hI@oc9#jrO@T',
                    account='NEXT_PATHWAY_PARTNER.us-east-1',
                    warehouse='INFA_POC',
                    database=database_name,
                    schema=schema_name
                    )
    
query1 = '''SELECT PROCEDURE_NAME FROM INFORMATION_SCHEMA.PROCEDURES WHERE PROCEDURE_SCHEMA = %s AND PROCEDURE_CATALOG = %s;'''
tuple1 = (schema_name, database_name)
cur = conn.cursor()
cur.execute(query1, tuple1)
sp = cur.fetchall()

for sp_name in sp:
    print(sp_name)