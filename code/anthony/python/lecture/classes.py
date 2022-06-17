
class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.price > other.price

    def discount(self, amount):
        # .25
        return self.price - self.price * amount


# apple = Fruit("Apple", .5)
# banana = Fruit("Banana", .5)
# kiwi = Fruit("Kiwi", 1)

# print(kiwi.discount(.5))
# print(kiwi.price)

# if kiwi > banana:
#     print("Kiwis are delicious")


# Ask the user for fruits and prices until done
fruits = []
while True:
    name = input("Enter name of fruit, or done to calculate total: ")
    if name == "done":
        break
    price = input(f"Enter the price of {name}: $")

    fruit = Fruit(name, price)
    fruits.append(fruit)

# Tally up total price of all fruits purchased
total = 0
for fruit in fruits:
    total += fruit.discount(1.1)

print(f"Total: ${total:.2f}")
