import random

print("⚔️ CHARACTER STAT GENERATOR ⚔️")
print()

def rollDice6():
    return random.randint(1,6)

def rollDice8():
    return random.randint(1,8)

playGame = "yes"

while playGame == "yes":
    nameWarrior = input("Name  your warrior > ")
    print("Their health hp is ", rollDice6()*rollDice8())
    playGame = input("Again? > ")
    print()
