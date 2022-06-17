pets = ['dog', 'cat', 'bird', 'snake', 'hedgehog', 'par']
"""  when you want to compare """
for pet in pets:
    print(pet)

    if len(pet) in pets:
        if len(pet) >3 and len(pet) <6:
         print(f'{pet}s are the coolest pets#!')

        
#__________________________________________________#
""" when you want to loop over a number of time """

for x in range(3,10):
    print('hello world')
print(list(range(3,10)))
        
#__________________________________________________#
"""when you want to make changes """

for i in range(len(pets)):
    pets[i] = pets [i] + 's'

print(pets)

    
#__________________________________________________#
"""While a condition remains true, continue to loop"""
num = 0
while num <10:
    print('hello world', num)
    num = num + 1

#__________________________________________________#

while True:
    print('Forever loop')
    user_input = input("Enter 'done' to leave loop: ")

    if user_input == "done":
        break
#__________________________________________________#
foods = []
bad_food = ["pizza", "burger", "fries"]

while True:
    food = input("Enter your favorite food or 'done' to quit: ")

    if food == "done":
        break
    if food in bad_food:
        print(f"{food} ..... are you sure?")
        continue
    foods.append(food)

print(food)

if len(food) <5:
    print("Nice choices")
elif len(foods) >5:
    print("You must be a foodie")