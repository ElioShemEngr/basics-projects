print("A N I M A L S 🤠 F A R M")
print()

exit = None

while exit != "yes":
    animal: str = input("What animal do you want? : ")

    if animal == "cow":
        print("A 🐮 cow goes moo")
        print()
    elif animal == "dog":
        print("A 🐶 dog goes Wof Wof")
        print()
    elif animal == "cat":
        print("A 😺 cat goes Miau Miau")
        print()
    else:
        print("I dont this animal, sorry!")

    exit = input("Do you want to exit? > ")
