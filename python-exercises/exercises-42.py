import random

bingoCard = [["0", "0", "0"],
             ["0","BINGO", "0"],
             ["0", "0", "0"]
            ]

def numberCard():
  numberRand = random.randint(1,90)
  return numberRand

filas = len(bingoCard)
columnas = len(bingoCard[0])

for fila in range(filas):
  for columna in range(columnas):
    if bingoCard[fila][columna] == "BINGO":
      continue
    else:
      bingoCard[fila][columna] = numberCard()

print()
print(f"{bingoCard[0][0]:<5} | {bingoCard[0][1]:^5} | {bingoCard[0][2]:>5}")
print("---------------------")
print(f"{bingoCard[1][0]:<5} | {bingoCard[1][1]:^5} | {bingoCard[1][2]:>5}")
print("---------------------")
print(f"{bingoCard[2][0]:<5} | {bingoCard[2][1]:^5} | {bingoCard[2][2]:>5}")