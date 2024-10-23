print("E P I C   🪨  📄  ✂️   B A T T L E")
print()

print("Select your move (R, P or S)")
print()

player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
print()

if player1 == "R":
    if player2 == "R":
        print("Player 1 and Player 2 have tied")
    elif player2 == "P":
        print("Player 2 Win!")
    elif player2 == "S":
        print("Player 1 Win!")
    else:
        print("Player 2 select incorrect")

elif player1 == "P":
    if player2 == "P":
        print("Player 1 and Player 2 have tied")
    elif player2 == "S":
        print("Player 2 Win!")
    elif player2 == "R":
        print("Player 1 Win!")
    else:
        print("Player 2 select incorrect")

elif player1 == "S":
    if player2 == "S":
        print("Player 1 and Player 2 have tied")
    elif player2 == "R":
        print("Player 2 Win!")
    elif player2 == "P":
        print("Player 1 Win!")
    else:
        print("Player 2 select incorrect")

else:
    print("Player 1 select incorrect")
