import os, time

taskList = []

f = open("tasklist.txt", "r")
taskList = eval(f.read())
f.close()

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
        for x in taskList:
            for y in x:
                print(f"{y:^10} | ", end='')
            print("")
        time.sleep(3)
        os.system("cls")
        print()
    elif selectView == "2":
        selectPriority =  input("Alto, Medio, Bajo > ").capitalize()
        if selectPriority == "Alto":
            for x in taskList:
                if "Alto" in x:
                    for y in x:
                        print(f"{y:^10} | ", end='')
                else:
                    continue
                print("")
            time.sleep(3)
            os.system("cls")
        elif selectPriority == "Medio":
            for x in taskList:
                if "Medio" in x:
                    for y in x:
                        print(f"{y:^10} | ", end='')
                else:
                    continue
                print("")
            time.sleep(3)
            os.system("cls")
        elif selectPriority == "Bajo":
            for x in taskList:
                if "Bajo" in x:
                    for y in x:
                        print(f"{y:^10} | ", end='')
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
    print("Edit")
    print()
    print("What task want edit? ")
    taskOld = input("> ").capitalize()
    print()
    print("What task want Add? ")
    taskNew = input("> ").capitalize()
    day = input("Day > ").capitalize()
    important = input("Important > ").capitalize()
    taskResume = [taskNew, day, important]
    for row in taskList:
        if taskOld in row:
            taskList.remove(row)
            taskList.append(taskResume)
    time.sleep(1)
    os.system("cls")

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
    
    f = open("tasklist.txt", "w")
    f.write(str(taskList))
    f.close()

