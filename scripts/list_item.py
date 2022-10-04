from genericpath import exists
import os 
import pathlib
import shutil

log_fle_name='log/item_list.log'
log_file = open(log_fle_name, "w")

# end the root folder with / last


root_folder='D:/NPW/Projects/CACF/cacf-postfiles_2022-09-21-135101/lot1/'
dest_root_folder=os.path.join(root_folder,'ITEM/')

for root, dirs, files in os.walk(root_folder, topdown=True):
   for file in files:
       if file.endswith(".item"):
           rel_folder_path=root.replace(root_folder,'')
           source_file_name=os.path.join(root_folder,rel_folder_path,file).replace("\\","/")
           dest_folder_path=os.path.join(dest_root_folder,rel_folder_path).replace("\\","/")
           dest_file_name=os.path.join(dest_folder_path,file).replace("\\","/")
           log_file.write(source_file_name + "|" + dest_file_name + "\n")

           if(not(os.path.exists(dest_folder_path))):
                   pathlib.Path(dest_folder_path).mkdir(parents=True, exist_ok=True)
           try:
              shutil.copy(source_file_name,dest_file_name)
           except:
               log_file.write("-----ERROR-----")  

