import string

def rotcypher():
    letters = list(string.ascii_lowercase)

    user_string = list(input("Please enter a string: "))
    rotation = int(input("Enter your rotation: "))

    rot = []
    for i, user_string in enumerate(user_string):
        if i + rotation < 25:
            rot.append(letters[i + rotation])
        else:
            rot.append(letters[i - rotation])
    return "".join(rot)

print(rotcypher())