from os import listdir
from os.path import isfile, join
#from iics_xml_parse import convert_xml_to_json
import datetime

xml_dir = r"C:\Users\kafle\Documents\Komhar\IAF\xml"
log_dir = r"C:\Users\kafle\Documents\Komhar\IAF\log"
json_dir = r"C:\Users\kafle\Documents\Komhar\IAF\json"
resource_group = "iA-Financial-ResourceGroup"
factory_name = "iA-Financial-DF"
pipeline_name = "dummy_pipeline"
pipeline_suffix = "_komhar"
log_file= log_dir + "\\" + "convert_xml_to_json_" + datetime.date.today().strftime("%Y%m%d") + ".txt"

xml_files = [file for file in listdir(xml_dir) if file.endswith(".xml") and isfile(join(xml_dir, file))]

for file in xml_files:
    print("Converting: " + file)
    convert_xml_to_json(xml_dir + "\\" + file, json_dir)

json_files = [file for file in listdir(json_dir) if file.endswith(".json") and isfile(join(json_dir, file))]
for file in json_files:
    pipeline_name = file.replace(".json", pipeline_suffix)
    json_full_file_name = json_dir + "\\" + file

    command_to_deploy = f"az datafactory pipeline list --resource-group {resource_group} --factory-name {factory_name} "
    print(command_to_deploy)
    os.system(command_to_deploy)