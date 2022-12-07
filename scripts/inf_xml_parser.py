import os
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

#define the XML files directory path
folder = r"D:\NPW\POC\Ilmarinen\PowerCenter\test"

#defining empty list to store the output value for each combination
session_temp_list = []
workflow_temp_list = []
worklet_temp_list = []
wf_worklet_temp_list = []

for directory in os.listdir(folder):
    #Running a loop to read all the files from the directory
    for filename in os.listdir(os.path.join(folder, directory)):
        print(filename)
        f = os.path.join(folder+'\\'+directory, filename)
        print(f)
        # checking if it is a file
        if os.path.isfile(f):
            #Filetring the files only with the XML extension
            if f.endswith(".XML") or f.endswith(".xml"):
                for root_tree in f:
                    #Parsing each file to generate the XML file Element tree
                    tree = ET.parse(f)
                    for i in tree.getroot():
                        for j in i:
                            for k in j:
                                for l in k:
                                    if k.tag == 'SESSION':
                                        stemp = directory,filename,k.attrib["MAPPINGNAME"],k.attrib["NAME"]
                                        session_temp_list.append(stemp)
                                    if k.tag == 'WORKLET':
                                        if l.tag == 'SESSION':
                                            stemp = directory,filename,l.attrib["MAPPINGNAME"],l.attrib["NAME"]
                                            session_temp_list.append(stemp)
                                            wktemp = directory,filename,l.attrib["NAME"],k.attrib["NAME"]
                                            worklet_temp_list.append(wktemp)
                                    if k.tag == 'WORKFLOW':
                                        if l.tag == 'SESSION':
                                            stemp = directory,filename,l.attrib["MAPPINGNAME"],l.attrib["NAME"]
                                            session_temp_list.append(stemp)
                                            wtemp = directory,filename,l.attrib["NAME"],k.attrib["NAME"]
                                            workflow_temp_list.append(wtemp)
                                        if l.tag == 'TASKINSTANCE':
                                            if l.attrib["TASKTYPE"] == 'Session':
                                                wtemp = directory,filename,l.attrib["TASKNAME"],k.attrib["NAME"]
                                                workflow_temp_list.append(wtemp)
                                            if l.attrib["TASKTYPE"] == 'Worklet':
                                                wfwktemp = directory,filename,l.attrib["TASKNAME"],k.attrib["NAME"]
                                                wf_worklet_temp_list.append(wfwktemp)
                                        if l.tag =='WORKLET':
                                            for o in k:
                                                print(o.tag,l.tag)
                                                if o.tag == 'TASKINSTANCE':
                                                    if o.attrib["TASKTYPE"] == 'Session':
                                                        wktemp = directory,filename,o.attrib['TASKNAME'],k.attrib['DESCRIPTION']
                                                        wfwktemp = directory,filename,k.attrib['DESCRIPTION'],l.attrib['DESCRIPTION']
                                                        worklet_temp_list.append(wktemp)
                                                        wf_worklet_temp_list.append(wfwktemp)



    #Converting output of each list to DataFrame
    df_s = pd.DataFrame(session_temp_list,columns = ['Folder Name','FileName','Mapping_Name','Session_Name']).drop_duplicates()
    df_w = pd.DataFrame(workflow_temp_list, columns = ['Folder Name','FileName','Session_Name','Workflow_Name']).drop_duplicates()
    df_wk = pd.DataFrame(worklet_temp_list, columns = ['Folder Name','FileName','Session_Name','Worklet_Name']).drop_duplicates()
    df_wfwk = pd.DataFrame(wf_worklet_temp_list, columns = ['Folder Name','FileName','Worklet_Name','Workflow_Name']).drop_duplicates()

    #session_1 = pd.merge(pd.merge(df_s,df_wk, on=['Session_Name','FileName'],how= 'outer'),df_w, on=['Session_Name','FileName'],how = 'outer')
    #print(session_1.columns)


    # Creating empty DataFrames to store the output of the merged dataframes to create a lineage
    session_1 = pd.DataFrame(columns=['Folder Name','FileName','Mapping_Name', 'Session_Name', 'Worklet_Name','Workflow_Name'])
    session_1 = pd.merge(pd.merge(df_s,df_wk, on=['Folder Name','FileName','Session_Name'],how= 'outer'),df_w, on=['Folder Name','FileName','Session_Name'],how = 'outer')
    # session_1 = session_1.drop(['FileName_y','FileName'],axis=1)
    session_1 = session_1.drop_duplicates()
    #
    #
    workflow_1 = pd.DataFrame(columns=['Folder Name','FileName','Mapping_Name', 'Session_Name', 'Worklet_Name','Workflow_Name_x','Workflow_Name_y'])
    workflow_1 = pd.merge(session_1,df_wfwk,on =['Folder Name','FileName','Worklet_Name'],how = 'outer')
    workflow_1['Workflow_Name_x'] = workflow_1['Workflow_Name_x'].fillna(workflow_1['Workflow_Name_y'])
    workflow_1 = workflow_1.drop(['Workflow_Name_y'],axis=1)
    workflow_1 = workflow_1.drop_duplicates()

workflow_1.index = np.arange(1, len(workflow_1) + 1)
workflow_1.index.rename('Sr. No.', inplace=True)
# #Exporting the list of Elements to CSV
workflow_1.to_excel('D:\\NPW\\POC\\Ilmarinen\\output\\1.xlsx')