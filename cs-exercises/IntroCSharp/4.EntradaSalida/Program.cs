using System;

namespace EntradaSalida
{
    class Program
    {
        static void Main()
        {
            string nombre;

            // Salida de Datos
            Console.WriteLine("Ingrese su nombre : ");
            // Entrada de Datos
            nombre = Console.ReadLine();

            Console.WriteLine();
            Console.WriteLine("El nombre ingresado es : ");
            Console.WriteLine(nombre);

        }
    }
}