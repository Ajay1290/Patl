import os
import json

from .utils import create_folder
from .utils import create_file
from .utils import remove_folder
from .utils import remove_file
from .utils import change_dir


def create_dir(d):
    """A Recrusive Fuction which creates folders and files.
    
    Parameters:
    ===========
    d : a dict object which contains 
        structure of files and folder.
    """
    tp_dirs = list(d.keys())
    for dir in tp_dirs:
        if type(d[dir]) == type({}):
            create_folder(dir)
            change_dir(dir)
            create_dir(d[dir])
        elif d[dir] == None:
            create_file(dir)
    change_dir('../')


def remove_dir(d):
    """A Recrusive Fuction which remove folders and files.
    
    Parameters:
    ===========
    d : a dict object which contains 
        structure of files and folder.
    """
    tp_dirs = list(d.keys())
    for dir in tp_dirs:
        if type(d[dir]) == type({}):
            change_dir(dir)
            remove_dir(d[dir])
            remove_folder(dir)
        elif d[dir] == None:
            remove_file(dir)
    change_dir('../')


def create_Alldirs():
    """A Fuction which creates folders and files."""
    f = open(f'{os.getcwd()}\\patl.json', 'r')
    d = json.load(f)
    create_dir(d)
    f.close()
    print("| All folders and files are created successfully.")


def remove_Alldirs():
    """A Fuction which removes folders and files."""
    f = open(f'{os.getcwd()}\\patl.json', 'r')
    d = json.load(f)
    remove_dir(d)
    f.close()
    print("| All folders and files are removed successfully.")