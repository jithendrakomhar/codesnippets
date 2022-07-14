import os
xml_root_folder='D:/NPW/POC/CACF/cacf-postfiles_2022-07-01-092003/Talend/XML/'
log_file='./log/file_list_prop.txt'


with open(log_file,'w+') as logfile:

    for root, dirs, files in os.walk(xml_root_folder, topdown=True):
     for file in files:
        if file.endswith(".properties"):
            xml_file_name_abs=os.path.join(root,file)
            logfile.write(xml_file_name_abs.replace("\\","/")+"\n")