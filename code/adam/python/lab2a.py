import random
print("What is the name of the last person you called? ")
person = input("> ")

print("Where was the last place you ate out at? ")
place = input("> ")

print("Type in any verb, action word. ")
verb = input("> ")

adjetive = []
print("Now, give me three adjetives or 'done'? ")

while True:
    adjetive_in = input("> ")
    
    if adjetive_in == "done":
        print("goodbye")
        
       
    else:
        adjetive.append(adjetive_in)
        if len(adjetive) == 3:
            break

print(f"""
When i was at the beach with {person},
we hoped on the dragon to go to {place}
to play {verb} with {person}.
We had to leave early {person} felt, {adjetive[random.randint(0,2)]}.

""")