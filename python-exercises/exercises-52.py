import os, time

inventory = []

def menu():
    print("--- INVENTORY. ---")
    print("------------------")
    print("| 1. Add item    |")
    print("| 2. View items  |")
    print("| 3. Remove item |")
    print("| 4. Quit        |")
    print("------------------")

def addItem():
    print("Add Item")
    print()
    itemNew = input("Item to add > ")
    inventory.append(itemNew)
    print("Added...")
    time.sleep(2)
    os.system("cls")

def viewItem():
    print("View Items")
    print()
    listAmount = []
    for i in inventory:
        if i in listAmount:
            continue
        else:
            listAmount.append(i)
    for i in listAmount:
        print(f"{i} : {inventory.count(i)}")
    time.sleep(2)
    os.system("cls")
    
def removeItem():
    print("Remove Items")
    print()
    itemRem = input("Item to remove > ")
    if itemRem in inventory:
        inventory.remove(itemRem)
    else:
        print()
        print("The Item is not in the Inventory...")

    time.sleep(2)
    os.system("cls")

try :
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()

    while True:
        menu()
        selectUser = input("> ")
        os.system("cls")
        if selectUser == "1":
            addItem()
        elif selectUser == "2":
            viewItem()
        elif selectUser == "3":
            removeItem()
        elif selectUser == "4":
            exit()
        else:
            print("Select a correct option...")
            time.sleep(2)
            os.system("cls")

        f = open("inventory.txt", "w")
        f.write(str(inventory))
        f.close()

except Exception as err :
    print()
    print("Error! : The base file has not been found ")
    print(err)