import os
import json

def create_folder(file):
    try:
        os.mkdir(file)
    except Exception:
        pass

def create_file(file):
    try:
        open(file, 'w')
    except Exception:
        pass

def remove_folder(file):
    try:
        os.rmdir(file)
    except Exception:
        pass

def remove_file(file):
    try:
        os.remove(file)
    except Exception:
        pass

def change_dir(dir):
    try:
        os.chdir(dir)
    except Exception:
        pass

def _getDirs(name):
    try:
        a = os.listdir(name)
    except NotADirectoryError:
        a = None

    return a

def wite_to_file(d):
    with open('patl.json', 'w', encoding="utf-8") as f:
        json.dump(d, f, indent=4, sort_keys=True)