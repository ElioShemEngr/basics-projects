import time, os

def menu():
    print("---- 🧮APP CALCULADORA🧮 ----")
    print("Bienvenidos...")
    print()
    print("------ MENU ------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")
    print("6. Potencia")
    print("7. Salir")
    print("------------------")
    print("Ingrese una opcion")
    user = int(input("> "))
    return user