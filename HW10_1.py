isra_dict: dict ={
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_Kilometer": 22145,
    "gdp_billion": 450
}

# a
print("get(capital): ", isra_dict.get("capital"));
# b
print("keys: ", isra_dict.keys());
# c
key_list: list = [key.upper() for key in isra_dict.keys()];
print(key_list);
# d
print("values: ", isra_dict.values());
# e
val_len: list = [len(str(val)) for val in isra_dict.values()];
print(val_len);
# f
print("items: ", isra_dict.items());
# g
isra_copy: dict = isra_dict.copy()
print(isra_copy);
# h
isra_dict.clear()
print(isra_dict);
# i
new_dict: dict = dict.fromkeys(isra_copy.keys(), None);
print(new_dict);

# j
del isra_copy["currency"];
# print(isra_copy);

# k
print(isra_copy.pop("area_Kilometer"));
# print(isra_copy);

# l
isra_copy.update({"national_sport": "Soccer", 'population_millions': 9.4})
print(isra_copy);