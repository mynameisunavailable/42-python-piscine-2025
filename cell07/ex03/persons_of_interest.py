def famous_births(scientists: dict) -> None:
    scientists = scientists.values()
    scientists_s = sorted(scientists, key = lambda x: x["date_of_birth"])
    # print(scientists_s)

    for item in scientists_s:
        # print(item)
        fullname = item["name"]
        dob = item["date_of_birth"]
        print(f"{fullname} is a great scientist born in {dob}.")
            

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)