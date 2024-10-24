#Este ejercicio se realiza en la Base de Datos de Replit del DIA 61
#Crear un twitter
import datetime, os, time

tweets = []

f = open("Tweetet.txt", "r")
tweets = eval(f.read())
f.close()

def menu():
    print("--- Tweeter ---")
    print()
    print("1: Add Tweet")
    print("2: View Tweet")
    print("3: Exit")
    print()


def addTweet():
    print("Add Tweet")
    print()
    print("Escriba su Tweet :")
    tweetIn = input("> ")
    timestamp = datetime.datetime.now()
    tweets.append([timestamp, tweetIn])
    print("Added...")

def viewTweet():
    print("View tweet")
    print()
    print("How many tweets do you want to see?")
    quantity = int(input(">"))
    for row in tweets[:quantity][::-1]:
        print(f"{row[0]} : {row[1]}")
    
while True:
    menu()
    selectUser = input("> ")
    os.system("cls")
    if selectUser == "1":
        addTweet()
        time.sleep(2)
        os.system("cls")
    elif selectUser == "2":
        viewTweet()
        time.sleep(2)
        os.system("cls")
    elif selectUser == "3":
        exit()
    else:
        print("Select a valid option...")
        time.sleep(2)
        os.system("cls")
    
    f = open("Tweetet.txt", "w")
    f.write(str(tweets))
    f.close()


