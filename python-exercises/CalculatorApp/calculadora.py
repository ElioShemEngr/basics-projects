def calculadora(user, x, y):
    match user:
        case 1:
            return x + y
        case 2:
            return x - y
        case 3:
            return x * y
        case 4:
            return x / y
        case 5:
            return x % y
        case 6:
            return x ** y
        case _:
            print("Ingrese una opcion correcta...")

def operacion(user):
    x = int(input("x > "))
    y = int(input("y > "))
    resultado = calculadora(user, x, y)
    return resultado
