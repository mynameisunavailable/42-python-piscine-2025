# !usr/bin/env python3

first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
result = first_num * second_num

print(f"{first_num} x {second_num} = {result}")

if result < 0:
    print("This number is negative.")
elif result > 0:
    print("This number is positive.")
elif result == 0:
    print("This number is positive and negative.")