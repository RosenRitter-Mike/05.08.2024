def remove_key_from_dict(dictionary: dict):
    dictionary.popitem()


def clear_all(dictionary: dict):
    dictionary = { }


a = {'x': 1, 'y': 2}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)

# pop works clear does not as you can see by running the code this is because popitem uses a built-in
# function of dictionary and clear_all does not.
# to clear_all efectively dict.clear() should be used.
