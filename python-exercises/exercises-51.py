import os, time

orderPizzas = []

def menu():
    print("---Elios  Pizza---")
    print("- The best taste -")
    print("------------------")
    print("| 1. Add Pizzas  |")
    print("| 2. View Pizzas |")
    print("| 3. Quit        |")
    print("------------------")

def addPizza():
    try :
        print("Add Pizza")
        print()
        name = input("Name : ")
        toppings = input("Toppings : ")
        size = input("Size (s/m/l) : ")
        quantity = int(input("Quantity : "))
        if size == "s":
            price = 9.99 * quantity
            priceFinal = round(price, 3)
            order = [name, toppings, size, quantity, priceFinal]
            orderPizzas.append(order)
        elif size == "m":
            price = 19.99 * quantity
            priceFinal = round(price, 3)
            order = [name, toppings, size, quantity, priceFinal]
            orderPizzas.append(order)
        elif size == "l":
            price = 29.99 * quantity
            priceFinal = round(price, 3)
            order = [name, toppings, size, quantity, priceFinal]
            orderPizzas.append(order)
        else:
            print(f"the size {size} is not valid...")
        time.sleep(2)
        os.system("cls")
    except :
        print("ERROR! : The value of quantity is not integer")
        time.sleep(2)
        os.system("cls")

def viewPizza():
    print("View Pizza")
    print()
    for row in orderPizzas:
        print()
        for i in row:
            print(f"{i:^10} | ", end='')
    print()
    time.sleep(2)
    os.system("cls")

try :
    f = open("eliopizza.txt", "r")
    orderPizzas = eval(f.read())
    f.close()

    while True:
        menu()
        selectUser = input("> ")
        os.system("cls")
        if selectUser == "1":
            addPizza()
        elif selectUser == "2":
            viewPizza()
        elif selectUser == "3":
            exit()
        else:
            print("Select a correct option...")
            time.sleep(2)
            os.system("cls")

        f = open("eliopizza.txt", "w")
        f.write(str(orderPizzas))
        f.close()

except Exception as err :
    print()
    print("Error! : The base file has not been found ")
    print(err)
