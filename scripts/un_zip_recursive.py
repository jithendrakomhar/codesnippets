import os 
import zipfile

folder_path='E:\old\Jithu_New\MRAsnowflake'

for root,dirs,files in os.walk(folder_path):
    for file in files:
        if file.endswith(".zip"):
            src_file=os.path.join(folder_path,file)
            dest_file=src_file.replace('.zip','')
            print(src_file,dest_file)
            with zipfile.ZipFile(src_file, 'r') as zip_ref:
                zip_ref.extractall(dest_file)