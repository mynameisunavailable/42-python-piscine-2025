#!usr/bin/env python3

def shrink(string: str):
    print(string[:8])

def enlarge(string: str):
    length = len(string)
    while length < 8:
        string += "Z"
        length += 1
    print(string)

from sys import argv

argc = len(argv)
if argc == 1:
    print("none")
else:
    for i in range(1, argc):
        word = argv[i]
        wordlen = len(word)
        # print(word, wordlen)
        if wordlen > 8:
            shrink(word)
        elif wordlen < 8:
            enlarge(word)
        elif wordlen == 8:
            print(word)