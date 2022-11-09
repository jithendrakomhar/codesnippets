import snowflake.connector
import os
from os.path import exists as file_exists

list_path = input("Enter file path:")
folder_path = input("Enter final folder path:")

file1 = open(list_path,"r")
datafile = file1.read().splitlines() 
print(datafile)
for i in datafile:
    temp3 = i.split('.')
    database_name = temp3[0]
    schema_name = temp3[1]
    final_path = database_name + '.' + schema_name
    if not os.path.isdir(os.path.join(folder_path, final_path)):
        os.makedirs(os.path.join(folder_path, final_path))
    
    conn = snowflake.connector.connect(
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
    
    for procedure in sp:
        if not file_exists('store_procedures.txt'):
            with open(os.path.join(folder_path, final_path) + '\\' + 'store_procedures.txt', 'a') as f:
                f.write(procedure[0]+"\n")
            f.close()
        
        query2 = '''SELECT ARGUMENT_SIGNATURE FROM INFORMATION_SCHEMA.procedures WHERE PROCEDURE_NAME = %s AND PROCEDURE_SCHEMA= %s;'''
        tuple2 = (procedure[0], schema_name)
        cur.execute(query2, tuple2)
        
        parameters = []
        data = cur.fetchone()[0]
        temp1 = data.strip("()")
        temp2 = temp1.split(',')
        for i in temp2:
            temp = i.split(' ')
            parameters.append(temp[-1])
        
        str1 = ""
        for i in parameters:
            str1 = str1 + i + ','
        str1 = str1.rstrip(str1[-1])
        
        query3 = '''use {};'''
        cur.execute(query3.format(database_name))
        query4 = '''select get_ddl('procedure', '{}.{}.{}({})')'''
        cur.execute(query4.format(database_name, schema_name, procedure[0], str1))
        output = cur.fetchone()[0]
        with open(os.path.join(folder_path, final_path) + '\\' + procedure[0]+'.sql', 'w') as f:
            f.write(output)
        f.close()