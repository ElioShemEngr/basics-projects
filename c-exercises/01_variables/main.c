// Directivas del Preprocesador y variables

// Librerias
#include <stdio.h>

// Macro
#define PI 3.1416

// Variable Global
int x = 3;

int main() // funcion Principal
{
    // Variables Locales
    int y = 7;
    float suma = 0;

    suma = (x + y) * PI;

    printf("El resultado de suma es : %.2f", suma);

    return 0;
}
