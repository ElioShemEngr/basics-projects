import os, time

def play():
    print("This Song is ready...")
    time.sleep(5)

while True:
    print("🎵 MyPOD Music Player 🎵")
    time.sleep(2)
    print()
    print("Press 1 to Play")
    time.sleep(1)
    print("Press 2 to Exit")
    time.sleep(1)
    print("Press anything else to see the menu again")
    time.sleep(1)
    print()
    selectUser: str = input(">")
    if selectUser == "1":
        play()
        os.system("cls")
    elif selectUser == "2":
        exit()
    else:
        os.system("cls")
        continue