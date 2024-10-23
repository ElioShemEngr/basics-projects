print("Fill-in the blank Lyrics 🎶")
print()

counter = 1

while True:
    print("Never going to ___ you up")
    enterWord = input("> ")
    if enterWord == "give":
        print("Well done, it only took you ", counter, " attempts!")
        break
    else:
        print("Nope, try again")
        print()
        counter += 1
