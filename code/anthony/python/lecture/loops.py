pets = ["dog", "cat", "bird", "snake", "hedgehog", "parrot"]


""" Iterate over a list """
# for pet in pets:
#     if len(pet) > 3 and len(pet) < 6:
#         print(f"{pet}s are the coolest pets!")


""" Iterate a given number of times """
# for x in range(10):
#     print("Hello World", x)

# print(list(range(10, 3, -1)))

""" Iterate over list and have ability to change elements within that list """
# for i in range(len(pets)):
#     pets[i] = pets[i] + "s"

# print(pets)

""" While a condition remains true, continue to loop """
# num = 0
# while num < 10:
#     print("Hello World", num)
#     num += 1

# while True:
#     print("Forever loop")
#     user_input = input("Enter 'done' to leave loop: ")

#     if user_input == "done":
#         break

foods = []
bad_foods = ["pizza", "burger", "fries"]
while True:
    food = input("Enter your favorite food or 'done' to quit: ")
    if food == "done":
        break
    if food in bad_foods:
        print(f"{food}... are you sure?")
        continue
    foods.append(food)

print(foods)

if 2 < len(foods) < 5:
    print("Nice choices")
elif len(foods) >= 5:
    print("You must be a foodie")
