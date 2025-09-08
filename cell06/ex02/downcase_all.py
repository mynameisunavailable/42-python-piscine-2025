#!usr/bin/env python3

def downcase_it(string: str) -> str:
    return string.lower()

from sys import argv

argc = len(argv)
if argc == 1:
    print("none")
else:
    for i in range(1, argc):
        word = argv[i]
        print(word.lower())