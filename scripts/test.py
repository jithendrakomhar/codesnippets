import os 
import pandas as pd 

file_path='log/xml_log.txt'

df = pd.read_csv(file_path,header=None,names=["Sequence"])

log_fle_name='log/split_job.txt'
log_file = open(log_fle_name, "w")

for index,row in df.iterrows():
    jobname= row[0].split("\\")[0] + "|"+  row[0].split("\\")[-1].split("|")[0] + "|" + row[0] + "\n"
    log_file.write(jobname)

