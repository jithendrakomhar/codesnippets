import os 
import pandas as pd
from datetime import datetime
from datetime import date
import json 

pipe_line_src_path = r'D:\NPW\Projects\IAF\IA-Financial-ADF\pipeline'
# pipe_line_tgt_path = r'D:\NPW\Projects\IAF\IAF-Pipelines\
# df = pd.read_csv(json_list)

now = datetime.now()
date_yyymmdd=now.strftime('%Y%m%d')

for root,dirs,files in os.walk(pipe_line_src_path,topdown=True):
    for file in files:
        json_file=os.path.join(pipe_line_src_path,file)
        print(json_file)
        f_json_file = open(json_file)
        json_data = json.load(f_json_file)
        print(json_data['properties']['folder'])
        break
