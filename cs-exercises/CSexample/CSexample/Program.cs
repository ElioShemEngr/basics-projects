using System;

namespace PromedioNotas
{
    class Program 
    {
        static void Main()
        {
            Console.Title = "Mi Programa";
            Console.WriteLine("Presiona una tecla para continuar...");
            ConsoleKeyInfo tecla = Console.ReadKey();
            Console.Beep();
            Console.WriteLine($"\nHas presionado: {tecla.Key}");

        }

    }
}