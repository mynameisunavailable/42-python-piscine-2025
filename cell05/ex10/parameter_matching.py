#!usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    password = sys.argv[1]
    attempt = input("What was the parameter? ")
    if attempt == password:
        print("Good job!")
    else:
        print("Nope, sorry...\n") #need new line here?