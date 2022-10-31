from operator import index
from pydoc import doc
import pandas as pd
from requests import head 

log_fle_name="log/job_list.txt"
log_file = open(log_fle_name, "w")

excel_file=r"F:\Python\codesnippets\src\cacf.xlsx"

df=pd.read_excel(excel_file,header=0,sheet_name='Job Raw Uniq')

#job_name=r"WFSRP\WFSRP\process_mr\PROJET_JOB\WFSRP_VIEWBUILDER_SPARK_TRANSACTION_0.2.item"
#print("_".join(job_name.split("\\")[-1].split("_")[:-1]))

for job_name in df["Job Name"]:
   log_file.write(job_name.split("\\")[-1])
   log_file.write("\n")
