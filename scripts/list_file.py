import os
xml_root_folder='D:/NPW/Projects/CACF/test-zip/ITEM'
log_file='./log/file_list_item.txt'


with open(log_file,'w+') as logfile:

    for root, dirs, files in os.walk(xml_root_folder, topdown=True):
     for file in files:
        if file.endswith(".item"):
            xml_file_name_abs=os.path.join(root,file)
            logfile.write(xml_file_name_abs.replace("\\","/")+"\n")