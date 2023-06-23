"""
dddddd
"""

from pathlib import Path


project_path = Path(__file__).resolve().parents[1]

# Data Path
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

temp_path = input_path / 'temp'
temp_path.mkdir(exist_ok=True)

maps_path = output_path / 'maps'
maps_path.mkdir(exist_ok=True)

geo_path = output_path / 'geo'
geo_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
