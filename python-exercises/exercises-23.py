import random

print("Infinite Dice 🎲")

userSide: int = int(input("How many sides? > "))
playGame: str = "yes"

def rollDice(sides):
    print("You rolled ", random.randint(1,sides))

while playGame == "yes":
    rollDice(userSide)
    playGame = input("Again? > ")
