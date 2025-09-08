#!usr/bin/env python3

from sys import argv

argc = len(argv)
if argc == 1:
    print("none")
else:
    print("parameters:", argc - 1)
    for i in range(1, argc):
        word = argv[i]
        print(f"{word}: {len(word)}")