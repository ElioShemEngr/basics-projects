import os, time

listEmail = []

def addEmail():
    emailA = input("Email Add > ")
    if emailA in listEmail:
        print("The email is in List")
        time.sleep(1)
        os.system("cls")
    else:
        listEmail.append(emailA)
        time.sleep(1)
        os.system("cls")
    
def removeEmail():
    emailR = input("Email Remove > ")
    if emailR in listEmail:
        listEmail.remove(emailR)
        time.sleep(1)
        os.system("cls")
    else:
        print()
        print(f"{emailR} is not in the List...")
        time.sleep(2)
        os.system("cls")

def showEmails():
    print("List of Emails")
    print()
    counter = 1
    for index in range(len(listEmail)):
        print(f"{index}.- {listEmail[index]}")
        counter += 1
    itemsList = len(listEmail)
    time.sleep(itemsList)
    os.system("cls")

def getSpam():
    numberSpam = int(input("Numbers of Spam > "))
    counter = 1
    for index in range(numberSpam):
        print(f"Email {counter}")
        counter += 1
        print()
        print(f"Dear {listEmail[index]}")
        print("""
it has come to ourattention that you're missing out on 
the amazing Replit 100 days of code. we insist you do it 
rigth away. If you don't we will pass on your email 
address to every spammer we've ever encontered and also 
sign you to the My Little Pony mewsletter, because 
that's neat. We migth jus to that anyway.""")
        print()
        print("Love and hugs,")
        print()
        print("Ian Spammington III")
        time.sleep(3)
        os.system("cls")

while True:
    print("------------------")
    print("SPAMMER Inc. eMail")
    print("------------------")
    print()
    print(" ===   MENU   === ")
    print()
    print("Select an number...")
    print()
    print("1. Add eMail")
    print("2. Remove eMail")
    print("3. Show eMails")
    print("4. Get Spamming")
    print("5. Exit")
    print()
    selectUser = input("> ")
    os.system("cls")

    if selectUser == "1":
        addEmail()
    elif selectUser == "2":
        removeEmail()
    elif selectUser == "3":
        showEmails()
    elif selectUser == "4":
        getSpam()
    elif selectUser == "5":
        exit()
    else:
        print("Number select is not Menu")
        print("Please, Select a correct option...")
        time.sleep(3)
        os.system("cls")
