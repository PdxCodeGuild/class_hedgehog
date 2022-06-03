person = {
    "first_name": "Ron",
    "last_name": "Weasley",
    "age": 50,
    "height": 154
}

# Updating a key: value pair
person["age"] = 51

# Adding a key: value pair to dictionary
person["fav_color"] = "Orange"

# Will throw an error if key does not exist
# print(person["house"])

# .get() method
height = person.get("height")  # returns None if no key found

# remove key: value pair
del person["age"]
# print(person)

# Check if key exists in dictionary
# if "last_name" in person:
#     print(person["last_name"])
# else:
#     print(f"{person['first_name']} has no last_name.")

# for key in person:
#     print(f"{key}: {person[key]}")

# .values() returns an iterable of all values within dictionary
# print(person.values())
# for value in person.values():
#     print(value)

# .keys() returns an iterable of all keys within a dict
# print(person.keys())

# .items() return both keys and values of a dict
# print(person.items())
for key, value in person.items():
    print(key, value)


# computer = {
#     "cpu": "Intel i7",
#     "memory": 16,
#     "storage": 2048,
#     "graphics": "RTX 3070",
#     "stuff": ["monitor", "mouse", "keyboard"],
#     "users": {
#         "johnsnow": "kingofnorth",
#         "harry": "boywholived"
#     }
# }

# print(computer)


inventory = {}

while True:
    item_name = input("Enter item name or done to quit: ")
    if item_name == "done":
        break
    item_price = input(f"Enter the price of {item_name}")

    inventory[item_name] = item_price

print(inventory)
