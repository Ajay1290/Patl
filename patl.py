import os
import json
from optparse import OptionParser

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

def create_dirs(d):
    tp_dirs = list(d.keys())
    for dir in tp_dirs:
        if type(d[dir]) == type({}):
            create_folder(dir)
            change_dir(dir)
            create_dirs(d[dir])
        elif d[dir] == None:
            create_file(dir)
    change_dir('../')


def remove_dirs(d):
    tp_dirs = list(d.keys())
    for dir in tp_dirs:
        if type(d[dir]) == type({}):
            change_dir(dir)
            remove_dirs(d[dir])
            remove_folder(dir)
        elif d[dir] == None:
            remove_file(dir)
    change_dir('../')

def print_V(option, opt, value, parser):
    print("v0.0.1-beta")

def create_Alldirs(option, opt_str, value, parser):
    f = open(f'{os.getcwd()}\\patl.json', 'r')
    d = json.load(f)
    create_dirs(d)
    f.close()
    print("| All folders and files are created successfully.")


def remove_AllDirs(option, opt_str, value, parser):
    f = open(f'{os.getcwd()}\\patl.json', 'r')
    d = json.load(f)
    remove_dirs(d)
    f.close()
    print("| All folders and files are removed successfully.")

parser = OptionParser()
parser.add_option('-v', '--version', 
                  action='callback',
                  callback=print_V,
                  help="to show current version of patl.")
parser.add_option('-c', '--create',
                  action='callback',
                  callback=create_Alldirs,
                  help="a JSON file's path goes here | default=patl.json")
parser.add_option('-r', '--remove',
                  action='callback',
                  callback=remove_AllDirs,
                  help="to remove files and folders as given in config file")
(options, args) = parser.parse_args()