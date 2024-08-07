countries = [ {'name': 'Israel', 'population': 9.3, 'birth': 1948},
{'name': 'United States', 'population': 331.9, 'birth': 1776}, {'name': 'Japan',
'population': 125.8, 'birth': 660 }, {'name': 'Australia', 'population': 25.7, 'birth': 1901},
{'name': 'Canada', 'population': 38.0, 'birth': 1867} ];

# q1
print("filter pop > 30 mil", list(filter(lambda x: x["population"] > 30, countries)));
# q2
print("filter birth > 1800", list(filter(lambda x: x["birth"] > 1800, countries)));
# q3
cunt_n: list[str] = list(map(lambda x: x["name"], countries));
print(cunt_n);
# q4
cunt_b: list[int] = list(map(lambda x: x["birth"], countries));
print(cunt_b);
# q5
print("sorted by birth", sorted(countries, key=lambda country: country["birth"]));
# q6
print("sorted by population", sorted(countries, key=lambda country: country["population"]));