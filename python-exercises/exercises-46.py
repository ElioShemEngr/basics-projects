import os, time, random

characters = {"Mr Spock" : {"Intelligence" : 99, "Speed" : 25, "Strong" : 20},
              "Elio" : {"Intelligence" : 90, "Speed" : 70, "Strong" : 50},
              "Monica from Friends" : {"Intelligence" : 50, "Speed" : 40, "Strong" : 30},
              "Professor X" : {"Intelligence" : 90, "Speed" : 90, "Strong" : 10}}

def selectPc():
    return random.choice(list(characters.keys()))
    
def habilityGame():
    print("Choose your stat : Intelligence, Speed, Strong")
    selectHab = input("> ")
    print()
    print(f"{characters[selectChar]} : {characters[selectChar][selectHab]}")
    print(f"{characters[computer]} : {characters[computer][selectHab]}")
    
def menuGame():
    print("TOP TRUMPS")
    print("----------")
    print()
    print("Characters")
    print()
    print("Mr Spock")
    print("Elio")
    print("Monica from Friends")
    print("Professor X")
    print()
    print("Pick your Character")

while True:
    menuGame()   
    selectChar = input("> ")
    print()
    computer = selectPc()
    print(f"Computer has picked {computer}")
    print()
    if selectChar == "Mr Spock":
        print("Choose your stat : Intelligence, Speed, Strong")
        selectHab = input("> ")
        print()
        print(f"{selectChar} : {characters[selectChar][selectHab]}")
        print(f"{computer} : {characters[computer][selectHab]}")
        print()
        if characters[selectChar][selectHab] > characters[computer][selectHab]:
            print(f"{selectChar} Wins!!!")
        elif characters[selectChar][selectHab] < characters[computer][selectHab]:
            print(f"{computer} Wins!!!")
        else:
            print("Draw!!!")
        time.sleep(5)
        os.system("cls")
    elif selectChar == "Elio":
        print("Choose your stat : Intelligence, Speed, Strong")
        selectHab = input("> ")
        print()
        print(f"{selectChar} : {characters[selectChar][selectHab]}")
        print(f"{computer} : {characters[computer][selectHab]}")
        print()
        if characters[selectChar][selectHab] > characters[computer][selectHab]:
            print(f"{selectChar} Wins!!!")
        elif characters[selectChar][selectHab] < characters[computer][selectHab]:
            print(f"{computer} Wins!!!")
        else:
            print("Draw!!!")
        time.sleep(5)
        os.system("cls")
    elif selectChar == "Monica From Friends":
        print("Choose your stat : Intelligence, Speed, Strong")
        selectHab = input("> ")
        print()
        print(f"{selectChar} : {characters[selectChar][selectHab]}")
        print(f"{computer} : {characters[computer][selectHab]}")
        print()
        if characters[selectChar][selectHab] > characters[computer][selectHab]:
            print(f"{selectChar} Wins!!!")
        elif characters[selectChar][selectHab] < characters[computer][selectHab]:
            print(f"{computer} Wins!!!")
        else:
            print("Draw!!!")
        time.sleep(5)
        os.system("cls")
    elif selectChar == "Professor X":
        print("Choose your stat : Intelligence, Speed, Strong")
        selectHab = input("> ")
        print()
        print(f"{selectChar} : {characters[selectChar][selectHab]}")
        print(f"{computer} : {characters[computer][selectHab]}")
        print()
        if characters[selectChar][selectHab] > characters[computer][selectHab]:
            print(f"{selectChar} Wins!!!")
        elif characters[selectChar][selectHab] < characters[computer][selectHab]:
            print(f"{computer} Wins!!!")
        else:
            print("Draw!!!")
        time.sleep(5)
        os.system("cls")
    else:
        print("Select a correct option")
        time.sleep(5)
        os.system("cls")
