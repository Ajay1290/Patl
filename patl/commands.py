import argparse

from .core import create_Alldirs
from .core import remove_Alldirs


parser = argparse.ArgumentParser()

parser.add_argument('-c', '--create', action='store_true', help="To create files and folders as per patl.json file says")

parser.add_argument('-r', '--remove', action='store_true', help="To remove files and folders as per patl.json file says" )


def main():
    args = parser.parse_args()

    if args.create:
        create_Alldirs()

    if args.remove:
        remove_Alldirs()