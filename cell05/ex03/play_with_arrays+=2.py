#!usr/bin/env python3

list = [2, 8, 9, 48, 8, 22, -12, 2]

new_list = []
for i in list:
    if i > 5:
        new_list.append(i + 2)

# seen = set()
# unique_list = []
# for i in new_list:
#     if i not in seen:
#         unique_list.append(i)
#         seen.add(i)

# import collections
# new_list_counter = collections.Counter(new_list)
# for key, val in new_list_counter.items():
#     if val > 1:
#         for i in range(val - 1):
#             new_list.remove(key)

print(list)
print(set(new_list))