#!usr/bin/env python3

age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
add_age = 10
multiple = 1

while multiple <= 3:
    future = add_age * multiple
    print(f"In {future} years, you'll be {age + future} years old.")
    multiple += 1
