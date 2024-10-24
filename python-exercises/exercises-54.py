import os, time, random

taskList = []

files = os.listdir("Python/")
fileProgram = os.path.join("Python/", "tasklist.txt")#Path of Program File -> Principal

fileExists = True
try :
    f = open(fileProgram, "r")
    taskList = eval(f.read())
    f.close()
except:
    fileExists = False

'''
if "tasklist.txt" not in files:
    print ("Error: Quick save not found")
'''

f = open(fileProgram, "r")
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

backupFile = f"backup{random.randint(0,1000000000)}"
fileBackup = os.path.join("Python/","backupe55/", backupFile)##Path of BackUp-> Backup


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
    
    f = open(fileProgram, "w")
    f.write(str(taskList))
    f.close()

    if fileExists:
        try :
            os.mkdir("Python/backupE55")
        except:
            pass
        
        backupFile = f"backup{random.randint(0,1000000000)}"
        fileBackup = os.path.join("Python/","backupe55/", backupFile)##Path of BackUp-> Backup

        f = open(fileBackup, "w")
        f.write(str(taskList))
        f.close() 