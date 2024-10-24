print("Infinity Dice")
print()

def rollDice(sides):
    import random

    again = ""

    while again != "no":
        dice = random.randint(1,sides)
        print("You rolled ", dice)
        print()
        again = input("Roll again? > ")

userSide = int(input("How many Sides? > "))

rollDice(userSide)

