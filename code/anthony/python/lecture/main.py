
def addition(x, y):
    return x + y


def main():
    """ Grading """
    grade = int(input("Enter your grade: "))

    grade = addition(grade, 5)

    if grade >= 90:
        print("You got an A")
    elif grade >= 80:
        print("You got a B")
    elif grade >= 70:
        print("You got a C")


main()
