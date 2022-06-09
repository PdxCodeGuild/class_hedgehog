import string

def rotcypher():
    letters = list(string.ascii_lowercase)

    user_string = list(input("Please enter a string: "))

    rot = []
    for i, user_string in enumerate(user_string):
        if i + 13 < 25:
            rot.append(letters[i + 13])
        else:
            rot.append(letters[i - 13])
    return "".join(rot)

print(rotcypher())