import random

print("Infinite Dice 🎲")

userSide = int(input("How many sides? > "))
playGame = "yes"

def rollDice(sides):
    print("You rolled ", random.randint(1,sides))

while playGame == "yes":
    rollDice(userSide)
    playGame = input("Again? > ")
