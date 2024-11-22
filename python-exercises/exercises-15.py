print("Fill-in the blank Lyrics 🎶")
print()

counter: int = 1

while True:
    print("Never going to ___ you up")
    enterWord: str = input("> ")
    if enterWord == "give":
        print("Well done, it only took you ", counter, " attempts!")
        break
    else:
        print("Nope, try again")
        print()
        counter += 1
