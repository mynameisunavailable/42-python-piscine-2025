#!usr/bin/env python3

num = int(input("Enter a number less than 25\n"))

if num > 25:
    print("Error")
else:
    while num <= 25:
        print(f"inside the loop, my variable is {num}")
        num += 1