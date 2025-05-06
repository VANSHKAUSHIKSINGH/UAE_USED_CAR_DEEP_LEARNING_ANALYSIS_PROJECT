import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


ProjectName = "USED_CAR_PREDICTION"

list_of_files = [
    ".github/workflows/.gitkeep",     #where we use for CI/CD and .gitkeep is a convention used in Git to ensure that empty directories are tracked in a repository
    f"src/{ProjectName}/__init__.py",
    f"src/{ProjectName}/components/__init__.py",
    f"src/{ProjectName}/utils/__init__.py",
    f"src/{ProjectName}/config/__init__.py",
    f"src/{ProjectName}/config/configuration/__init__.py",
    f"src/{ProjectName}/pipeline/__init__.py",
    f"src/{ProjectName}/entity/__init__.py",
    f"src/{ProjectName}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
    
]
    
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
            
            
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    
    else:
        logging.info(f"file already exists: {file_path}")   
         