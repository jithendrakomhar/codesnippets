import os 
import xml.etree.ElementTree as ET


xml_root_folder='D:/NPW/POC/CACF/cacf-postfiles_2022-07-01-092003/Talend/XML_NEW/'

log_fle_name='xml_log.txt'
log_file = open(log_fle_name, "w")

for root, dirs, files in os.walk(xml_root_folder, topdown=True):
   for file in files:
       if file.endswith(".item"):
        xml_file_name_abs=os.path.join(root,file)
        xml_file_name_rel=xml_file_name_abs.replace(xml_root_folder,'')

        try:

            mytree = ET.parse(xml_file_name_abs)
            myroot = mytree.getroot()

            if(myroot.findall('node')):
                    for x in myroot.findall('node'):
                        component_name=xml_file_name_rel+"|"+x.attrib['componentName']+"\n"
                        log_file.write(component_name)

            else:
                    component_name=xml_file_name_rel+"|"+'No Talend Components Found'+"\n"
                    log_file.write(component_name)
        except:
               log_file.write(xml_file_name_rel+'| Not  a valid XML'+"\n")
log_file.close()