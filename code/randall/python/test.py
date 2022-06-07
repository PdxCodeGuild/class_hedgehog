def latest_letter(word): #passes word in
    highest_letter = sorted(word)[-1] #creates sorted list in alphabetic order and selects last item in string
    print(word)
    return highest_letter #returns the lasr letter in the string

print(latest_letter("poqzmry"))