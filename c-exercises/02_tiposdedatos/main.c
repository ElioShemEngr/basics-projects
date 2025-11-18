// Tipos de Datos

#include <stdio.h>

int main()
{
    char a = 'e';                // tamaño = 1byte rango: 0 al 255
    short b = -15;               // tamaño = 2 bytes rango: -128 al 127
    int c = 1024;                // tamaño = 2 bytes rango: -32768 al 32767
    unsigned int d = 1284;       // tamaño = 2bytes rango: 0 al 65535
    long e = 262144;             // tamaño = 4bytes rango: -2147483648 al 2147483648
    float f = 3.1415;            // tamaño = 4bytes rango: -3.4*10 al 3.4(10)
    double g = 0.000045;         // tamaño = 8bytes rango: -1.7*10 al 1.7(10)
    long double h = 2152.121312; // Igual que double

    printf("El char es : %c \n", a);
    printf("El short es : %i \n", b);
    printf("El entero es : %i \n", c);

    return 0;
}