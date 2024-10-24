'''
Algunos valores para distintos colores:

Color	    Value
Default	    0
Black	    30
Red	        31
Green	    32
Yellow	    33
Blue	    34
Purple	    35
Cyan	    36
White	    37

OPCION END:
Nota: Para el comando print(), tenemos distintas
configuraciones para imprimir el texto en
pantalla:

print("Texto", end="\n") -> sirve para realizar un salto de linea
print("Texto", end="\t") -> sirve para realizar una separacion tabulada
print("Texto", end="\v") -> sirve para realizar una separacion tabulada vertical


'''




def textColor(word,color):
    if color=="white":
        print("\033[37m", word, "\033[0m", sep="",end=" ")
    elif color=="cyan":
        print("\033[36m", word, "\033[0m", sep="",end=" ")
    elif color=="purple":
        print("\033[35m", word, "\033[0m", sep="",end=" ")
    elif color=="blue":
        print("\033[34m", word, "\033[0m", sep="",end=" ")
    elif color=="yellow":
        print("\033[33m", word, "\033[0m", sep=",",end=" ")
    elif color=="green":
        print("\033[32m", word, "\033[0m", sep="",end=" ")
    elif color=="red":
        print("\033[31m", word, "\033[0m", sep="",end=" ")
    elif color=="black":
        print("\033[30m", word, "\033[0m", sep="",end=" ")
    else:
        print("\033[0m", word, "\033[0m", sep="",end=" ")
    
textColor("Hola Mundo!","blue")
textColor("Eliosex","purple")
textColor("el mejor,","green")
textColor("ahora regreso al color por default","reset")
