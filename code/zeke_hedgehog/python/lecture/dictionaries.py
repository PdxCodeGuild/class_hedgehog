
# Dictionaries notes







person = {
    
    "first_name": "Ron", 
    "last_name" : "Weasley",
    "age" : 50,
}
##(updating age)
#person ["age"] = 51

# #Adding a key: value pair to dictionary
# person ["fav_color"] = "Orange"
print(person[" "])



# .get()method
height = person.get("height", False) # returns None if no key is found
print(height)

#how to remove a key value pair
del person["age"]
print(person)

# check if key exists in dictionary
if "last_name" in person:
    print(person["last_name"])
else:
    print(f"{person['first_name']} has no last_name.")

#