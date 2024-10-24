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
    if itemNew in myList:
        print(f"{itemNew} is in the List")
        time.sleep(2)
    else:
        myList.append(itemNew)

#Subrutina de Edit
def editList():
    print("what tasks do you want to edit? ")
    itemEdit = input("> ")
    print("What tasks do you add?")
    itemNew = input("> ")
    if itemEdit in myList:
        index = myList.index(itemEdit)
        myList[index] = itemNew
    else:
        print(f"The {itemEdit} is not in List")
        time.sleep(2)

#Subrutina de Remove
def removeList():
    print("what do you want to remove? ")
    itemRemove = input("> ")
    if itemRemove in myList:
        myList.remove(itemRemove)
    else:
        print()
        print(f"{itemRemove} no is in the List")
        time.sleep(2)

#Subrutina de Delete all tasks
def deleteList():
    deleteUser = input("what do you want to delete all items? ")
    if deleteUser == "yes":
        myList.clear()
    else:
        print("Return the principal menu...")
        time.sleep(2)


while True:
    print("------------------")
    print("To Do List Manager")
    print("------------------")
    print()
    print(" ===   MENU   === ")
    print("Select an option..")
    print()
    print("1. View task")
    print("2. Add task")
    print("3. Edit task")
    print("4. Remove task")
    print("5. Delete all")
    print("6. Exit")
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
    elif selectUser == "4" or selectUser == "remove":
        removeList()
        os.system("cls")
    elif selectUser == "5" or selectUser == "remove":
        deleteList()
        os.system("cls")
    elif selectUser == "6" or selectUser == "exit":
        exit()
    else:
        print("Select an correct option...")
