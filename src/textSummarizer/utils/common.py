#Utility function which i will be using in my code frequently
import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations #package ensure that the datatype passed to a function is correct or not
from box import ConfigBox #with this package we can access dictionary values like d.key
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    reads yaml file and returns
    :param path_to_yaml: path like input
    :return: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    :param path_to_directories: list of path of directories
    :param verbose:
    :return:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB
    :param path: path of the file
    :return: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"