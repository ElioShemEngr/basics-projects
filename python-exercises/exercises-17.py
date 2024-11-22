print("One-Million-to-One")
print()

round: int = 1

while True:
    numberGuess: int = int(input("What is your guess?: "))

    if numberGuess == 50:
        print("Correct")
        break
    elif numberGuess < 50:
        print("Too low")
        round += 1
    elif numberGuess > 50:
        print("Too high")
        round += 1
    else:
        print("Input a correct value")
        continue

print("It took you ", round, "guesses to get it correct!")
