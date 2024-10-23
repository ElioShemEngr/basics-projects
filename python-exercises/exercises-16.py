print("E P I C   🪨  📄  ✂️   B A T T L E")
print()

countPlayer1 = 0
countPlayer2 = 0

while True:
    if countPlayer1 == 3:
        print("BOTTOM LINE")
        print("Player_1 = ", countPlayer1, "point(s)")
        print("Player_2 = ", countPlayer2, "point(s)")
        print("PLAYER 1 IS WIN!!!")
        break
    elif countPlayer2 == 3:
        print("BOTTOM LINE")
        print("Player_1 = ", countPlayer1)
        print("Player_2 = ", countPlayer2)
        print("PLAYER 2 IS WIN!!!")
        break
    else:
        print("Select your move (R, P or S)")
        print()

        player1 = input("Player 1 > ")
        player2 = input("Player 2 > ")
        print()

        if player1 == "R":
            if player2 == "R":
                print("Player 1 and Player 2 have tied")
                continue
            elif player2 == "P":
                print("Player2 +1 Point!")
                print()
                countPlayer2 += 1
            elif player2 == "S":
                print("Player1 +1 Point")
                print()
                countPlayer1 += 1
            else:
                print("Player 2 select incorrect")
                continue

        elif player1 == "P":
            if player2 == "P":
                print("Player 1 and Player 2 have tied")
                continue
            elif player2 == "S":
                print("Player2 +1 Point!")
                print()
                countPlayer2 += 1
            elif player2 == "R":
                print("Player1 +1 Point")
                print()
                countPlayer1 += 1
            else:
                print("Player 2 select incorrect")
                continue

        elif player1 == "S":
            if player2 == "S":
                print("Player 1 and Player 2 have tied")
                continue
            elif player2 == "R":
                print("Player2 +1 Point!")
                print()
                countPlayer2 += 1
            elif player2 == "P":
                print("Player1 +1 Point")
                print()
                countPlayer1 += 1
            else:
                print("Player 2 select incorrect")
                continue

        else:
            print("Player 1 select incorrect")
