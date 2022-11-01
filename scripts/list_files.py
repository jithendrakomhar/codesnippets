import os

folder_path=r"D:\NPW\POC\Zaloni Workflows\Zaloni Workflows"
log_file=r"log/list_files.log"

f_log_fil= open(log_file,"w")

for root,folder_list,file_list in os.walk(folder_path):
    for file in file_list:
        f_log_fil.write(root+"|"+file+"\n")