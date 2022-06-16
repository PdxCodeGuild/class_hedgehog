def open_file(file_path):
    with open(file_path) as file:
        file = file.read()

    words = file.split(",")

    words.pop(4)

    with open(file_path, "w") as file:
        file.write(",".join(words))


open_file("words.csv")
