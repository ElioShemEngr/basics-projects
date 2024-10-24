
f = open("highscore.txt", "r")

score = f.read().split("\n")
print(score)
print()

highScore = 0
name = None

for row in score:
    data = row.split()
    if data != []:
        if int(data[1]) > highScore:
            highScore = int(data[1])
            name = data[0]

print(f"The Winner is {name} with highscore of {highScore}")

f.close()



