def average(student_dict: dict) -> int:
    length = len(student_dict)
    # sum(student_dict.values())
    total = 0
    for i in student_dict:
        total += student_dict[i]

    return total / length

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")