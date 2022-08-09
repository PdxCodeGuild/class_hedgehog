

number_grade = int(input("Enter your grade \n\t> "))

grade_table = {
    "10": "A+",
    "9": "A",
    "8": "B",
    "7": "C",
    "6": "D",
}

key = number_grade // 10

letter_grade = grade_table.get(str(key), "F")

print(f"You got a(n) {letter_grade}")