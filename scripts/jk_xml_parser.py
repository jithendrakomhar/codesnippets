import xml.etree.ElementTree as ET
tree = ET.parse(r'D:/NPW/POC/Ilmarinen/PowerCenter/exporttivakvar.xml')
root = tree.getroot()

element_list=[]

# for elem in root:
#        for child in elem:
#         print(child.tag, child.attrib)

# print(root.tag)
# parent = root.find('.//INSTANCE/..').tag

# print(parent)
#get all elements

for elem in root.iter():
    if elem.tag not in element_list:
        element_list.append(elem.tag)

print(element_list)

#get specific element

for elm_in_list in element_list:
    print(elm_in_list)
    for elem in root.iter(elm_in_list):
        elem_atrrib=[]
        for key in elem.attrib:
            if key not in elem_atrrib:
                elem_atrrib.append(key)
    print(elem.tag,elem_atrrib)