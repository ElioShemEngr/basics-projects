#include <stdio.h>

int main()
{
    // 0. Hola Mundo!
    printf("Hola Mundo desde C!\n");
    printf("Mi nombre es ElioshemDev!\n");

    // 1. Variables
    // Integer
    int age = 30;
    int year = 2025;
    // float
    float tail = 1.78;
    // char
    char letra = 'A';

    printf("Tienes %d anos de edad \n", age);
    printf("Tu altura es de %.2f \n", tail);
    printf("El ano actual es %d \n", year);
    printf("Esta es la letra : %c", letra);

    return 0;
}

// Ejecutar en una terminal integrada con la siguiente declaracion
//  gcc main.c -o main -> (para crear un ejecutable)
// luego ejecutamos
//./main.exe
