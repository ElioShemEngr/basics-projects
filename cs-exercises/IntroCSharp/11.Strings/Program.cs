using System;

namespace Strings
{
    class Program
    {
        static void Main()
        {
            // Strings
            string greating= "Hola";
            greating += " Mundo";

            Console.WriteLine(greating);

            // Concatenacion
            string name = "Elio";
            string message = "Bienvenido a C#";
            Console.WriteLine(name + ", " + message);
            // Interpolacion
            Console.WriteLine($"{name}, {message}");

            // Metods in string
            string frase = "  C# es un lenguaje poderoso  ";
            Console.WriteLine(frase.Trim());
            Console.WriteLine(frase.ToUpper());
            Console.WriteLine(frase.Trim().Replace("poderoso", "moderno"));
            Console.WriteLine(frase.Contains("lenguaje"));

            // Formateo de Cadenas
            double precio = 1234.567;
            Console.WriteLine($"Precio: {precio:C}"); // Formato moneda
            Console.WriteLine($"Número: {precio:N2}"); // 1,234.57


        }
    }
}