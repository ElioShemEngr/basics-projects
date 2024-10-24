import os, time


cList = []

exit = ""
while exit != "yes":
    print("NAME REGISTER")
    print()
    print("Insert Data: ")
    usFirstName = input("First Name > ").strip().capitalize()
    usLastName = input("Last Name > ").strip().capitalize()

    usNameFinal = f"{usFirstName} {usLastName}"

    print()
    print(usNameFinal)
    print()
    if usNameFinal in cList:
        print(f"ERROR: {usNameFinal} - Duplicate name")
    else:
        cList.append(usNameFinal)
        print(cList)
    print()
    exit = input("Exit? > ")
    
    time.sleep(2)
    os.system("cls")
