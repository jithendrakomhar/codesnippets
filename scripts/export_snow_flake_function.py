import snowflake.connector
import os
from os.path import exists as file_exists

list_path = r"F:\Python\codesnippets\log\function_list.txt"
folder_path = r"F:\Python\codesnippets\log\Snow_flake_functions"

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
    
    query1 = '''SELECT FUNCTION_NAME FROM INFORMATION_SCHEMA.FUNCTIONS WHERE FUNCTION_SCHEMA = %s AND FUNCTION_CATALOG = %s;'''
    tuple1 = (schema_name, database_name)
    cur = conn.cursor()
    cur.execute(query1, tuple1)
    sp = cur.fetchall()
    
    for function in sp:
        if not file_exists('functions.txt'):
            with open(os.path.join(folder_path, final_path) + '\\' + 'functions.txt', 'a') as f:
                f.write(function[0]+"\n")
            f.close()
        
        query2 = '''SELECT ARGUMENT_SIGNATURE FROM INFORMATION_SCHEMA.FUNCTIONS WHERE FUNCTION_NAME = %s AND FUNCTION_SCHEMA= %s;'''
        tuple2 = (function[0], schema_name)
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
        query4 = '''select get_ddl('function', '{}.{}.{}({})')'''
        cur.execute(query4.format(database_name, schema_name, function[0], str1))
        output = cur.fetchone()[0]
        with open(os.path.join(folder_path, final_path) + '\\' + function[0]+'.sql', 'w') as f:
            f.write(output)
        f.close()