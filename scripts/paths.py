"""
dddddd
"""

from pathlib import Path



project_path = Path('.').resolve().parent
print(project_path)

data_path = project_path / 'data'
input_path = data_path / 'input'
output_path = data_path / 'output'


temp_path = input_path / 'temp'
maps_path = output_path / 'maps'
shps_path = output_path / 'shps'

input_path.mkdir(exist_ok=True)
output_path.mkdir(exist_ok=True)
temp_path.mkdir(exist_ok=True)
maps_path.mkdir(exist_ok=True)
shps_path.mkdir(exist_ok=True)


# import os
# import shutil

#shutil.rmtree(temp_path, ignore_errors=True)
#shutil.rmtree(output_path, ignore_errors=True)

#os.makedirs(output_path, exist_ok=True)
#os.makedirs(temp_path, exist_ok=True)
#os.makedirs(maps_path, exist_ok=True)
