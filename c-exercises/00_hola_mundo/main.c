#include <stdio.h>

int main()
{
    // 0. Hola Mundo!
    printf("I like pizza!\n");
    printf("It's really good!\n");

    // 1. Variables
    int age = 30;
    int year = 2025;

    printf("You are %d years old\n", age);
    printf("The year is %d", year);

    return 0;
}

// Ejecutar en una terminal integrada con la siguiente declaracion
//  gcc main.c -o main -> (para crear un ejecutable)
// luego ejecutamos
//./main.exe
