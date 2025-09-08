#!usr/bin/env python3

from sys import argv

argc = len(argv)
if argc != 3:
    print("none")
else:
    keyword = argv[1]
    string = argv[2]
    string_list = string.split()
    count = 0
    for i in string_list:
        if keyword == i:
            count += 1
    
    if count == 0:
        print("none")
    else:
        print(count)