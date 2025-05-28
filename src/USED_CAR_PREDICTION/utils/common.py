import os
from box.box import Box
from box.exceptions import BoxValueError
import yaml
from USED_CAR_PREDICTION import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a Box object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Raises:
        valueError: If the file is not found or cannot be read.
        e: empty file error.
        
    Returns:
        Box: Contents of the YAML file as a Box object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list ofdirectories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories are created. Defaults to False.
            
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data:dict):
    """save json file
    
    Args:
        path (Path): path to json file
        data (dict): data to save in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file save at :{path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data
    
    Args:
        path (Path): path to json file
        
    Returns:
        ConfigBox: data as class attributes instead of dictionary keys
    """
    with open(path, "r") as f:
        content = json.load(f)
        
    logger.info(f"json file loaded succesfully from :{path}")
    
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    
    Args:
        data (Any): data to save in binary file
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at :{path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary file
    
    Args:
        path (Path): path to binary file
        
    Returns:
        Any: object loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from :{path}")
    
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size of file in KB
    
    Args:
        path (Path): path to file
        
    Returns:
        str: size of file in KB
    """
    size_in_KB = round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_KB} KB"

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
                return base64.b64encode(f.read())
            
