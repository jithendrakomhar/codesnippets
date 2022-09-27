import os 
import xml.etree.ElementTree as ET

xml_dir='src/'
log_dir='log/'

xml_name='inf_sample.xml'

node_name='./POWERMART/REPOSITORY'
node_attribute='NAME'


xml_file_name=xml_dir + xml_name
log_fle_name=log_dir + xml_name + ".log"

log_file = open(log_fle_name, "w")


try:

    mytree = ET.parse(xml_file_name)
    myroot = mytree.getroot()

    for country in myroot.findall('country'):
        if country.attrib['name'] == 'Panama':
            print(country.find('rank').attrib['updated'])

    if(myroot.findall(node_name)):
        for node_nm in myroot.findall(node_name):
            node_attribute_value=node_nm.attrib[node_attribute]+"\n"
            log_file.write(node_attribute_value)

    else:
                        transform_name="No node with the name "  + node_name + " Found in XML"+"\n"
                        log_file.write(transform_name)
except:
        log_file.write(log_file+'| Not  a valid XML'+"\n")
log_file.close()