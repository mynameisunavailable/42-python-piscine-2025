#!usr/bin/env python3

num = float(input("Give me a number: "))


if num // 1 == num:
    print(int(num))
else:
    print(int(num // 1 + 1))