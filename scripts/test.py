import pandas as pd

test_dict = {"names":["Jithu","surya","ishu","Bhuvana"],"address":["Kota","Nellore","Atmakur","Hyderbad"]}

# for idx,key_name in enumerate(test_dict):
#     print(idx,key_name)
#     for attrib in test_dict[key_name]:
#         print(attrib)

df = pd.DataFrame(test_dict)

print(type(df['names'][0]))