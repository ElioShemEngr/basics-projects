using System;

namespace Bucles
{
    class Program
    {
        static void Main()
        {
            // Bucles
            // For
            for (int i = 0; i <= 10; i += 3) // True
            {
                Console.WriteLine($"Vuelta numero {i}");
            }

            Console.WriteLine();

            // While
            string salir = "";

            while (salir != "yes") // True
            {
                Console.WriteLine("Hola a todos saludos");
                Console.Write("Quieres Salir? > ");
                salir = Console.ReadLine()!;
            }

            Console.WriteLine();

            // Do...While
            int numero;

            do
            {
                Console.Write("Ingrese un número positivo: ");
                numero = int.Parse(Console.ReadLine());
            }
            while (numero <= 0);

            Console.WriteLine($"Ingresaste el número {numero}");

            // Mas adelante...
            // Foreach (Para iterar sobre una "Colección")

        }
    }
}