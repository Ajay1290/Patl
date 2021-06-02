import os
import json

from .utils import create_folder
from .utils import create_file
from .utils import remove_folder
from .utils import remove_file
from .utils import change_dir
from .utils import wite_to_file
from .utils import _getDirs


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
    print("Patl> All folders and files are created successfully.")


def remove_Alldirs():
    """A Fuction which removes folders and files."""
    f = open(f'{os.getcwd()}\\patl.json', 'r')
    d = json.load(f)
    remove_dir(d)
    f.close()
    print("Patl> All folders and files are removed successfully.")


def getdirs(l, j=None, d=None, fresh=True, ignored = []):
    """A Recrusive Fuction which scans folders and files.
    
    Parameters:
    ===========
    l : a list of dirs
    j : old key goes here in second iter.
    d : old dict goes here in second iter.
    fresh : To Tell wheter recrusive is first time or not.
    """
    if fresh:
        d = {}
    else:
        os.chdir(j)
        a = {}
    for i in l:
        print(i, )
        if fresh:
            dir = _getDirs(i)
            if i not in ignored:
                d[i] = dir
                if dir:
                    getdirs(dir, i, d, False, ignored)
                    os.chdir('../')
        else:
            dir = _getDirs(i)
            if i not in ignored:
                a[i] = dir
                d[j] = a
                if dir:
                    getdirs(dir, i, a, False, ignored)
                    os.chdir('../')
    return d

def scan_Alldirs():
    """A Fuction which scans folders and files."""
    ignore_this = [z.strip('/\n') for z in open('.patlignore', 'r').readlines()]
    lis = [u for u in os.listdir() if u not in ignore_this]
    d = getdirs(lis, ignored=ignore_this)
    wite_to_file(d)
    print("Patl> All folders and files are scanned successfully to patl.json.")


