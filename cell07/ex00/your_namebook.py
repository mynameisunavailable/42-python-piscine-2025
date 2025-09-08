def array_of_names(name_dict: dict) -> list[str]:
    name_list = []
    for firstname, lastname in name_dict.items():
        #capitalise first letter of first, last name
        name = firstname.capitalize() + " " + lastname.capitalize()
        name_list.append(name)
    
    return name_list

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))