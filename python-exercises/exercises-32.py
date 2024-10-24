import os, time

#Creamos una lista vacia
myList = []

#Subrutina de View
def viewList():
    print("My List")
    print()
    for i in myList:
        print(f"- {i}")
    print()

#Subrutina de Add
def addList():
    print("what do you want to add? ")
    itemNew = input("> ")
    myList.append(itemNew)

#Subrutina de Edit
def editList():
    print("what do you want to remove? ")
    itemRemove = input("> ")
    if itemRemove in myList:
        myList.remove(itemRemove)
    else:
        print()
        print(f"{itemRemove} no is in the List")
        time.sleep(2)

while True:
    print("------------------")
    print("To Do List Manager")
    print("------------------")
    print()
    print(" ===   MENU   === ")
    print("Select an option..")
    print()
    print("1. View")
    print("2. Add")
    print("3. Edit")
    print("4. Exit")
    print()
    selectUser = input("> ")
    os.system("cls")

    if selectUser == "1" or selectUser == "view":
        viewList()
        time.sleep(3)
        os.system("cls")
    elif selectUser =="2" or selectUser == "add":
        addList()
        os.system("cls")
    elif selectUser == "3" or selectUser == "edit":
        editList()
        os.system("cls")
    elif selectUser == "4" or selectUser == "exit":
        exit()
    else:
        print("Select an correct option...")
