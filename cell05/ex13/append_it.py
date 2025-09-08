#!usr/bin/env python3

from sys import argv

argc = len(argv)
if argc == 1:
    print("none")
else:
    for i in range(1, argc):
        word = argv[i]
        if word[-3:] != "ism":
            print(word, "ism", sep = "")