import os

while True:
    print("HIGH SCORE TABLE")
    print()
    f = open("highscore.txt", "a+")
    initialsName = input("INITIALS > ")
    scoreData = input("SCORE > ")
    f.write(f"{initialsName} {scoreData} \n")
    print("ADDED...")
    f.close()
    exit = input("Exit? y/n > ").lower().strip()
    if exit == "y":
        os.system("cls")
        break
    else:
        os.system("cls")
        continue
        
