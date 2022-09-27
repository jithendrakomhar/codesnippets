from genericpath import exists
import os 
import pathlib
import shutil
 
root_folder='D:/NPW/Projects/CACF/test-zip/'
dest_root_folder=os.path.join(root_folder,'ITEM/')

for root, dirs, files in os.walk(root_folder, topdown=True):
   for file in files:
       if file.endswith(".item"):
           rel_folder_path=root.replace(root_folder,'')
           source_file_name=os.path.join(root_folder,rel_folder_path,file).replace("\\","/")
           dest_folder_path=os.path.join(dest_root_folder,rel_folder_path).replace("\\","/")
           dest_file_name=os.path.join(dest_folder_path,file).replace("\\","/")
           print(source_file_name,dest_file_name)

           if(not(os.path.exists(dest_folder_path))):
                   pathlib.Path(dest_folder_path).mkdir(parents=True, exist_ok=True)
           try:
              shutil.copy(source_file_name,dest_file_name)
           except:
               print("-----ERROR-----")  

