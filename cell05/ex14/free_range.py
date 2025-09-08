#!usr/bin/env python3

from sys import argv

argc = len(argv)
if argc != 3:
    print("none")
else:
    num1 = argv[1]
    num2 = argv[2]
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print("not a number")
    # print(num1, type(num1))
    # print(num2, type(num2))
    num_list = []
    for i in range(num1, num2 + 1):
        num_list.append(i)
    print(num_list)