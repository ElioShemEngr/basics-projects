import random, os, time

# Bingo Card Initial
bingoCard = [["0", "0", "0"],
             ["0", "BINGO", "0"],
             ["0", "0", "0"]]

# Number of row and columns
row = len(bingoCard)
column = len(bingoCard[0])

# List Number Add Cart
listNumbers = []

randomNumber = random.randint(0,90)

for i in range(0,8):
    randomNumber = random.randint(1,90)
    if randomNumber is not listNumbers:
        listNumbers.append(randomNumber)
    else:
        continue

listNumbers.sort()

index = 0
for x in range(row):
    for y in range(column):
        if bingoCard[x][y] != "BINGO":
            bingoCard[x][y] = listNumbers[index]
            index +=1 
        else:
            continue

'''
print()
for x in range(len(bingoCard)):
    for y in range(len(bingoCard[x])):
        print(f"{bingoCard[x][y]:^5} | ", end='')
    print("")
    print("-----------------------")
print()
'''

calledNumber = 0

while True:
    print("Bingo Card Generator")
    print()

    for x in range(row):
        for y in range(column):
            if bingoCard[x][y] == calledNumber:
                    bingoCard[x][y] = "X"
            else:
                continue

    print()
    for x in range(row):
        for y in range(column):
            print(f"{bingoCard[x][y]:^5} | ", end='')
        print("")
        print("-----------------------")
    print()

    if bingoCard == [["X", "X", "X"], ["X", "BINGO", "X"], ["X", "X", "X"]]:
        print("You Have Won")
        break

    calledNumber = int(input("What number was called? > "))
    os.system("cls")

    
