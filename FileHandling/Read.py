# This program looks up for an existing file in the directory
from Tools.scripts.treesync import raw_input

__author__ = 'aseem'

from os.path import exists

print("Type the file name: ")
file = raw_input("> ")
if exists(file):
    txt_again = open(file, 'r')
    print(txt_again.read())
else:
    print("no such file")