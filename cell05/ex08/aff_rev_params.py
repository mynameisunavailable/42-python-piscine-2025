#!usr/bin/env python3

import sys

argc = len(sys.argv)
if argc == 1:
    print("none")
else:
    for i in reversed(range(argc)):
        print(sys.argv[i])