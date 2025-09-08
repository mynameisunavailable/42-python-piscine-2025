def find_the_redheads(name_dict: dict) -> list[str]:
    red_list = filter(lambda x: name_dict[x] == "red", name_dict)
    return list(red_list)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))