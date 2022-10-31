import os
import pandas as pd
import shutil

pipeline_path = r"D:\NPW\Projects\IAF\IA-Financial-ADF\pipeline"
folder_path = r"D:\NPW\Projects\IAF\all_pipelines"
file_list_path = r"D:\NPW\Projects\IAF\Iaf_Task_Flow_List.xlsx"

pipeline_list = os.listdir(pipeline_path)

dataframe1 = pd.read_excel(file_list_path)
col_values = dataframe1['Folder Name'].drop_duplicates()

for value in col_values:
    baseDir = folder_path
    if not os.path.isdir(os.path.join(baseDir, value)):
        os.makedirs(os.path.join(baseDir, value))

pipeline_ADF = dataframe1['ADF object Name']
for i in range(len(pipeline_ADF)):
    for j in range(len(pipeline_list)):
        if str(pipeline_ADF[i]) + ".json" == str(pipeline_list[j]):
            new_path = str(folder_path) + '\\' + str(dataframe1['Folder Name'][i]) + '\\'
            old_path = str(pipeline_path) + '\\' + str(dataframe1['ADF object Name'][i]) + '.json'
            shutil.copy2(old_path, new_path)

#dataframe1.to_excel(file_list_path)
