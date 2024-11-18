import os, time
import calculadora as calc
import menu

operaciones = {
    1: "suma",
    2: "resta",
    3: "multiplicacion",
    4: "division",
    5: "modulo",
    6: "potencia"
}

def main():
    while True:
        try:
            user = menu.menu()
            os.system("cls")
            
            if user in operaciones:
                print(f"Ingrese los valores para realizar la operación: {operaciones[user]}")
                resultado = calc.operacion(user)
                print()
                print("--------------------------------")
                print(f"El resultado es : {resultado}")
                print("--------------------------------")
                time.sleep(2)
                os.system("cls")

            elif user == 7:
                print("Saliendo del programa...")
                time.sleep(2)
                os.system("cls")
                exit()

            else:
                print("Ingrese una opcion de la lista...")
                time.sleep(3)
                os.system("cls")

        except ValueError:
            print("ERROR: Entrada no válida. Por favor, ingrese un número.")
            time.sleep(3)
            os.system("cls")

main()