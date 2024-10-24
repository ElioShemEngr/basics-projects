print("MokeBeasts Full-On MOkedex")
print()

mokeBeast = {}

def prettyPrint():
    for key, value in mokeBeast.items():
        print(f"{key:^10}", end=" | ")
        for subkey, subvalue in value.items():
            print(f"{subvalue:^10}", end=" | ")
        print("")


while True:
    name = input("Name : ")
    type = input("Type : ")
    hp = input("HP : ")
    mp = input("MP : ")
    mokeBeast[name] = {"type" : type, "hp" : hp, "mp" : mp}
    print()
    print(f"   Name    |    Type    |     HP     |     MP    ")
    prettyPrint()
    print()
