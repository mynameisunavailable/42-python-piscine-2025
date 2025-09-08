#!usr/bin/env python3

from sys import argv

argc = len(argv)
if argc != 2:
    print("none")
else:
    have_z = False
    for i in argv[1]:
        if i == "z":
            have_z = True
            print("z", end = "")
    if have_z == False:
        print("none")