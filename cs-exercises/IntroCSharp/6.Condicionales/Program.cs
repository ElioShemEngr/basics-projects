using System;

namespace Condicionales
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("----------------------------");
            Console.WriteLine("*** Mi Examen Secundaria ***");
            Console.WriteLine();
            
            int nota;

            Console.WriteLine("Cuanto Sacaste? : ");
            nota = int.Parse(Console.ReadLine()); // 10

            // Condicionales (if, else if, else)
            if (nota >= 16)
            {
                Console.WriteLine("Excelente");
            }
            else if (nota >= 12)
            {
                Console.WriteLine("Aprobado");
            }
            else
            {
                Console.WriteLine("Desaprobado");
            }
            Console.WriteLine();


            Console.WriteLine("--------------------------");
            Console.WriteLine("*** Mi Examen Primaria ***");
            Console.WriteLine();

            string calificacion;

            Console.WriteLine("Cual es la calificacion (A, B, C, D)? : ");
            calificacion = Console.ReadLine();

            // Condicionales (switch - case)
            switch (calificacion) 
            {
                case "A":
                    Console.WriteLine("Excelente");
                    break;
                case "B":
                    Console.WriteLine("Bueno");
                    break;
                case "C":
                    Console.WriteLine("Regular");
                    break;
                case "D":
                    Console.WriteLine("Deficiente");
                    break;
                default:
                    Console.WriteLine("Nota no valida");
                    break;
            }
        }
    }
}