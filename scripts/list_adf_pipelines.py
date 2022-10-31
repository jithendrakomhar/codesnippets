import os 

json_full_file_name = r"C:\Users\jithe\Downloads\IA-Financial-ADF\pipeline\foreach_test.json"
resource_group = "iA-Financial-ResourceGroup"
factory_name = "iA-Financial-DF"
pipeline_name = "dummy_pipeline"
pipeline_suffix = "_komhar"
command_to_deploy = f"az datafactory pipeline list --resource-group {resource_group} --factory-name {factory_name} "
print(command_to_deploy)
os.system(command_to_deploy)