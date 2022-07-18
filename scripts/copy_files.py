
from genericpath import exists
import os 
import pathlib
import shutil
import pandas as pd

file_list="log/file_list.txt"
root_folder='D:/NPW/POC/CACF/cacf-postfiles_2022-07-01-092003/Talend/XML/'
dest_root_folder='D:/NPW/POC/CACF/cacf-postfiles_2022-07-01-092003/Talend/XML_NEW/'

print("--------------Jithu-------------")

df = pd.read_csv(file_list)

for file in df["JobName"]:
    src_file=os.path.join(root_folder,file)
    dest_file=os.path.join(dest_root_folder,file)
    dest_dir_name=os.path.dirname(dest_file)

    if not os.path.exists(dest_dir_name):
           pathlib.Path(dest_dir_name).mkdir(parents=True, exist_ok=True)
           
    try:
        shutil.copy(src_file,dest_file)
    except:
        print("-----ERROR-----")   
    