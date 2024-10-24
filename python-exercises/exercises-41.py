print("Mokebeast")
print()

mokebeast= {"name" : None, "type" : None, "move" : None, "hp" : None, "mp" : None}

for key, value in mokebeast.items():
    mokebeast[key] = input(f" {key} : ")

print()

if mokebeast["type"] == "Electric":
    print('\033[33m', end ='')
    for key, value in mokebeast.items():
        print(f"{key} : {value}")
elif mokebeast["type"] == "Water":
    print('\033[34m', end ='')
    for key, value in mokebeast.items():
        print(f"{key} : {value}")
elif mokebeast["type"] == "Fire":
    print('\033[31m', end ='')
    for key, value in mokebeast.items():
        print(f"{key} : {value}")
else:
    print("The tyype is not correct!!")