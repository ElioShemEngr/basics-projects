import os, time, random

#Definimos subrutinas de Health and Strength
def heatlh():
    return ((random.randint(1,6) * random.randint(1,12)) / 2 ) + 10

def strength():
    return ((random.randint(1,6) * random.randint(1,12)) / 2 ) + 12

playGame = "yes"

while playGame == "yes":
    print("⚔️ CHARACTER BUILDER ⚔️")
    print()
    time.sleep(2)
    print("Name Your Legend: ")
    userName = input("> ")
    print("Character Type (Human, Elf, Wizard, Orc): ")
    userType = input("> ")
    print()
    print("--------------------------")
    print(userName)
    print("HEALTH   : ", heatlh())
    print("STRENGTH : ", strength())
    print()
    print("May your name go down in Legend")
    print("--------------------------")
    playGame = input("Again? > ")
    os.system("cls")


