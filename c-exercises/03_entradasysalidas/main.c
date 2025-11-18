// Entrada y Salidad de Datos

#include <stdio.h>

int main()
{
    int x;
    int y;
    int suma;

    printf("Calculadora\n");
    printf("Indica el primer numero : \n");
    scanf("%i", &x);

    printf("Indica el segundo numero : \n");
    scanf("%i", &y);

    suma = x + y;

    printf("EL resultado de la suma es : %i", suma);

    return 0;
}