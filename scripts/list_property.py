
from genericpath import exists
import os 
import pathlib
import shutil

root_folder='D:/NPW/POC/CACF/cacf-postfiles_2022-07-01-092003/Talend/XML/'
dest_root_folder='D:/NPW/POC/CACF/cacf-postfiles_2022-07-01-092003/Talend/XML1/'

for root, dirs, files in os.walk(root_folder, topdown=True):
   for file in files:
       if file.endswith(".properties"):
        
           rel_folder_path=root.replace(root_folder,'')
           source_file_name=os.path.join(root_folder,rel_folder_path,file).replace("\\","/").replace("XML/","").replace(".item",".properties") 
           dest_folder_path=os.path.join(dest_root_folder,rel_folder_path)
           dest_file_name=os.path.join(dest_folder_path,file).replace("\\","/").replace(".item",".properties") 
           print(source_file_name,dest_file_name)

           if(not(os.path.exists(dest_folder_path))):
                   pathlib.Path(dest_folder_path).mkdir(parents=True, exist_ok=True)
           try:
              shutil.copy(source_file_name,dest_file_name)
           except:
               print("-----ERROR-----")   

