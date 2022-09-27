import os 
import xml.etree.ElementTree as ET

xml_dir='src/'
log_dir='log/'


xml_name='inf_sample.xml'
xml_name='informatica_real.xml'
xml_file_name=xml_dir + xml_name

mytree = ET.parse(xml_file_name)
myroot = mytree.getroot()



for node in myroot.iter():
       if node.tag=='TRANSFORMATION':
                if node.attrib['NAME']=='exp_Src' :
                        for child_node in node.iter():
                                try:
                                        print(child_node.attrib['EXPRESSION'].replace("\n"," ") + "--- as ----" + child_node.attrib['NAME'] + ",")
                                except:
                                        print("\' \'" + " -- as --" + child_node.attrib['NAME'] + ",")