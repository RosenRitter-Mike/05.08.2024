actions: dict = {"add": "Adding item", "delete": "Deleting item", "update": "Updating item"};
act: str = input("input action: ");
print(actions.get(act));