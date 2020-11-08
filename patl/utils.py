import os

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