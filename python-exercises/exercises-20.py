print("Math Game")
print()

numberMult: int = int(input("Name your multiples > "))

score: int = 0
for i in range(1,13):
    print(i, " x ", numberMult)
    userNumber: int = int(input("> "))
    if userNumber == i*numberMult:
        print("Great Work!")
        print()
        score += 1
    else:
        print("Nope 🥲 The answer was ", i*numberMult)
        print()

print("Your Score is ", score, " out of 12")
