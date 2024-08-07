dict_acts: dict = {"lower": lambda x: x.lower(), "upper": lambda x: x.upper(), "len": lambda x: len(x), "reverse": lambda x: x[::-1]};
# # ____________________Test______________________________
# for act in dict_acts:
#     print("TestWorD", dict_acts.get(act)("TestWorD"));
word: str = input("Enter word: ");
action: str = input("Enter operation name (lower, upper, len, reverse): ");

print(f"\nword: {word}\naction: {action}\nresult: {dict_acts.get(action)(word)}");