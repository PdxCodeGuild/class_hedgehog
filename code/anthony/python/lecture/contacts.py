class Contact:
    def __init__(self,
                 first_name="",
                 last_name="",
                 number="",
                 email="",
                 address="",
                 birthday=""):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.address = address
        self.birthday = birthday

    def __str__(self):
        return f"""
        First Name: {self.first_name},
        Last Name: {self.last_name},
        Number: {self.number},
        Email: {self.email},
        Address: {self.address},
        Birthday: {self.birthday}
        """

    def get_properties(self):
        return """
        0) First Name
        1) Last Name
        2) Number
        3) Email
        4) Address
        5) Birthday
        """


def pick_one(contacts):
    print("Pick one:")
    for i, contact in enumerate(contacts):
        print(i, contact.first_name)
    selection = input("-> ")
    return int(selection)


contacts = [Contact("dave"), Contact("susan")]
menu = """
1) Create new contact
2) Search for contact
3) Edit contact
4) Delete contact
5) List all
6) Exit
"""
while True:
    choice = input(menu + "-> ")
    if choice == "1":
        contact = Contact()
        contact.first_name = input("Enter contacts first name: ")
        contact.last_name = input("Enter contacts last name: ")
        contact.number = input("Enter contacts number: ")
        contact.email = input("Enter contacts email: ")
        contact.address = input("Enter contacts address: ")
        contact.birthday = input("Enter contacts birthday: ")
        contacts.append(contact)
    elif choice == "2":
        # Add search by field
        selection = pick_one(contacts)
        print(contacts[selection])
    elif choice == "3":
        selection = pick_one(contacts)
        print(contacts[selection])
        print("What would you like to update:")
        print(contacts[selection].get_properties())
        option = input("-> ")
        if option == "0":
            contacts[selection].first_name = input(
                "Enter contacts first name: ")
        elif option == "1":
            contacts[selection].last_name = input("Enter contacts last name: ")
        elif option == "2":
            contacts[selection].number = input("Enter contacts number: ")
        elif option == "3":
            contacts[selection].email = input("Enter contacts email: ")
        elif option == "4":
            contacts[selection].address = input("Enter contacts address: ")
        elif option == "5":
            contacts[selection].birthday = input("Enter contacts birthday: ")

    elif choice == "4":
        # Confirm delete
        selection = pick_one(contacts)
        contacts.pop(selection)
    elif choice == "5":
        for contact in contacts:
            print(contact)
    else:
        print("Have a nice day!")
        break


"""
class Animal:
    def __init__(self, name, species, age=0, hungry=False):
        self.name = name
        self.species = species
        self.age = age
        self.hungry = hungry

    def __str__(self):
        return f"{self.species} is {self.age} years old. They are hungry: {self.hungry}"

    def say_hello(self):
        print(f"My name is {self.name}")

    def birthday(self):
        self.age += 1
        return self.age


bruce = Animal("Bruce", "hedgehog", hungry=True)

sally = Animal("Sally", "llama", 3)

kevin = Animal("Kevin", "penguin", 12)

sally.birthday()
sally.birthday()
age = sally.birthday()
print(sally)
"""
