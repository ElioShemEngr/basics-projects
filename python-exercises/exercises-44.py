import os, time

taskList = []

def menu():
    print("--- To Do List ---")
    print("Management  System")
    print("------------------")
    print("|    1. Add      |")
    print("|    2. View     |")
    print("|    3. Remove   |")
    print("|    4. Edit     |")
    print("|    5. Quit     |")
    print("------------------")

def addTask():
    print("Add")
    print()
    task = input("Task > ").capitalize()
    day = input("Day > ").capitalize()
    important = input("Important > ").capitalize()
    taskResume = [task, day, important]
    print("Task added...!!!")
    time.sleep(1)
    os.system("cls")
    return taskList.append(taskResume)

def viewTask():
    print("View")
    print()
    print("1. View All")
    print("2. View Priority")
    selectView = input("> ")
    if selectView == "1":
        for x in range(len(taskList)):
            for y in range(len(taskList[x])):
                print(f"{taskList[x][y]:^10} | ", end='')
            print("")
        time.sleep(3)
        os.system("cls")
        print()
    elif selectView == "2":
        selectPriority =  input("Alto, Medio, Bajo > ").capitalize()
        if selectPriority == "Alto":
            for x in range(len(taskList)):
                for y in range(len(taskList[x])):
                    if "Alto" in taskList[x]:
                        print(f"{taskList[x][y]} | ", end='')
                    else:
                        continue
                print("")
            time.sleep(3)
            os.system("cls")
        elif selectPriority == "Medio":
            for x in range(len(taskList)):
                for y in range(len(taskList[x])):
                    if "Medio" in taskList[x]:
                        print(f"{taskList[x][y]} | ", end='')
                    else:
                        continue
                print("")
            time.sleep(3)
            os.system("cls")
        elif selectPriority == "Bajo":
            for x in range(len(taskList)):
                for y in range(len(taskList[x])):
                    if "Bajo" in taskList[x]:
                        print(f"{taskList[x][y]} | ", end='')
                    else:
                        continue
                print("")
            time.sleep(3)
            os.system("cls")
        print()        

def removeTask():
    print("Remove")
    print()
    remove = input("What would you like to remove? > ")
    for x in taskList:
        if remove in x:
                taskList.remove(x)
    time.sleep(1)
    os.system("cls")

def editTask():
    pass

while True:
    menu()
    selectUser = input("> ")
    os.system("cls")

    if selectUser == "1":
        addTask()
    elif selectUser == "2":
        viewTask()
    elif selectUser == "3":
        removeTask()
    elif selectUser == "4":
        editTask()
    elif selectUser == "5":
        exit()
    else:
        print("Select a correct option...")
        time.sleep(2)
        os.system("cls")

