import os
import pandas as pd
import shutil
import json

found_count = 0
notfound_count = 0
pipeline_path = input("Enter pipeline folder path:")
folder_path = input("Enter final folder path:")
#path = "C:\\Users\\Dixit\\Downloads\\IA-Financial-ADF\\pipeline"
pipeline_list = os.listdir(pipeline_path)
for i in range(len(pipeline_list)):
    f = open(pipeline_path + '\\' + pipeline_list[i])
    data = json.load(f)
    f.close()
    if 'folder' in data['properties']:
        for element in data['properties']:
            for value in data['properties']['folder'].items():
                final_path = value[1]
            if not os.path.isdir(os.path.join(folder_path, final_path)):
                os.makedirs(os.path.join(folder_path, final_path))
            new_path = os.path.join(folder_path, final_path)
            old_path = str(pipeline_path) + '\\' + str(pipeline_list[i])
            shutil.copy2(old_path, new_path)
        found_count = found_count + 1
    else:
        notfound_count = notfound_count + 1
        print(pipeline_list[i])

print(found_count)
print(notfound_count)