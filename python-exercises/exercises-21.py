import random

myNumber = random.randint(1,100)

print("One-Million-to-One")
print()

round = 1

while True:
    numberGuess = int(input("What is your guess?: "))

    if numberGuess == myNumber:
        print("Correct")
        break
    elif numberGuess < myNumber:
        print("Too low")
        round += 1
    elif numberGuess > myNumber:
        print("Too high")
        round += 1
    else:
        print("Input a correct value")
        continue

print("It took you ", round, "guesses to get it correct!")