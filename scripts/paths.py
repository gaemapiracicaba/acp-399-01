"""
dddddd
"""

from pathlib import Path



project_path = Path('.').resolve().parent
print(f'Pasta do Projeto é: {project_path}')

data_path = project_path / 'data'
input_path = data_path / 'input'
output_path = data_path / 'output'


temp_path = input_path / 'temp'
maps_path = output_path / 'maps'
geo_path = output_path / 'geo'

input_path.mkdir(exist_ok=True)
output_path.mkdir(exist_ok=True)
temp_path.mkdir(exist_ok=True)
maps_path.mkdir(exist_ok=True)
geo_path.mkdir(exist_ok=True)
