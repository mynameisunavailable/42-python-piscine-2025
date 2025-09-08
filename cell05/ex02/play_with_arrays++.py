#!usr/bin/env python3

list = [2, 8, 9, 48, 8, 22, -12, 2]

new_list = []
for i in list:
    if i > 5:
        new_list.append(i + 2)

print(list)
print(new_list)