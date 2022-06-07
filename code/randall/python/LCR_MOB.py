#Randall, Stacy, Zane, Adrian, Wesley

"""LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}."""
from random import choice
pot = 0
players = []
dice = ["L","C","R","1","1","1"]
winner = ""
#var for pot

#list dictionaries

while True:
    player = input("Please enter player name or 'done' to begin game: ").lower().replace(' ', '')
    if player == "done":
        break
    else:
        players.append({"name":player, "chips":3})
#print(players)

#while loop
def roll():
    result = choice(dice)
    return result
#print(roll())
#enter names and "done"

#check if done

#append input to dict

#for loop player rolls 
while True:
    for player in players:
        if player.get("chips") + pot == len(players)*3:
            winner = player.get("name")
            break
    if winner:
        break
    for player in players:
        results = []
        if player.get("chips") == 1:
            results.append(roll())
        elif player.get("chips") == 2:
            results.append(roll())
            results.append(roll())
        elif player.get("chips") >= 3:
            results.append(roll())
            results.append(roll())
            results.append(roll())
        for result in results:
            if result == "R":               
                player["chips"] -= 1
                index = players.index(player) + 1
                index %= len(players)
                players[index]["chips"] += 1
            elif result == "L":
                player["chips"] -= 1
                index = players.index(player) - 1
                players[index]["chips"] += 1
            elif result == "C":
                player["chips"] -= 1
                pot += 1
print(winner)