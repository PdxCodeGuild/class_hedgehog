import random

# Get names from user until done


def get_users():
    players = []
    while True:
        player = input("Enter player name or 'done' to start: ")
        if player == 'done':
            break
        # {"name": "John", "chips": 3}
        players.append({"name": player, "chips": 3})
    return players


def main():
    play_again = "y"
    while play_again == "y":
        # list of dictionaries to store player data
        players = get_users()
        # center pot
        pot = 0
        # dice variable
        dice = ["L", "C", "R", ".", ".", "."]
        # winner
        winner = False
        # game loop (while no winner)
        while winner == False:
            # loop through users
            for i, player in enumerate(players):
                # determine number of dice (number of rolls
                # rolls = min(3, player["chips"])
                if player["chips"] > 2:
                    rolls = 3
                else:
                    rolls = player["chips"]
                # loop number of dice and roll dice
                for roll in range(rolls):
                    roll = random.choice(dice)
                    # determine outcome of each roll
                    if roll == "L":
                        players[i-1]["chips"] += 1
                        player["chips"] -= 1
                    elif roll == "C":
                        pot += 1
                        player["chips"] -= 1
                    elif roll == "R":
                        if i == len(players) - 1:
                            players[0]["chips"] += 1
                        else:
                            players[i+1]["chips"] += 1
                        player["chips"] -= 1

                # check for winner
                if player["chips"] + pot == len(players) * 3:
                    winner = player
        print(winner["name"] + " Wins!")
        play_again = input(
            "Would you like to play again? (yes/no): ").lower()[0]


main()
