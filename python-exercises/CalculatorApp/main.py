import os, time
import calculadora as calc
import menu

def main():
    while True:
        user = menu.menu()
        os.system("cls")

        if user == 1:
            print("Ingrese los dos valores a sumar:")
            resultado = calc.operacion(user)
            print()
            print("-------------------------------------")
            print(f"El valor de la suma es : {resultado}")
            print("-------------------------------------")
            time.sleep(2)
            os.system("cls")
            
        elif user == 2:
            print("Ingrese los dos valores a restar:")
            resultado = calc.operacion(user)
            print()
            print("-------------------------------------")
            print(f"El valor de la resta es : {resultado}")
            print("-------------------------------------")
            time.sleep(2)
            os.system("cls")

        elif user == 3:
            print("Ingrese los dos valores a multiplicar:")
            resultado = calc.operacion(user)
            print()
            print("-------------------------------------")
            print(f"El valor de la multiplicacion es : {resultado}")
            print("-------------------------------------")
            time.sleep(2)
            os.system("cls")

        elif user == 4:
            resultado = calc.operacion(user)
            print()
            print("-------------------------------------")
            print(f"El valor de la division es : {round(resultado, 2)}")
            print("-------------------------------------")
            time.sleep(2)
            os.system("cls")

        elif user == 5:
            print("Ingrese los dos valores a modular:")
            resultado = calc.operacion(user)
            print()
            print("-------------------------------------")
            print(f"El valor del  modulo es : {resultado}")
            print("-------------------------------------")
            time.sleep(2)
            os.system("cls")

        elif user == 6:
            print("Ingrese la base('x') y el exponente('y'):")
            resultado = calc.operacion(user)
            print()
            print("-------------------------------------")
            print(f"El resultado es : {resultado}")
            print("-------------------------------------")
            time.sleep(2)
            os.system("cls")
            
        elif user == 7:
            print("Saliendo del programa...")
            time.sleep(2)
            os.system("cls")
            exit()

main()