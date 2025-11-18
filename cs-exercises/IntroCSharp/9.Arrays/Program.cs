using System;

namespace Arrays
{
    class Program
    {
        static void Main()
        {
            // Arrays Strings
            string[] names = new string[3];

            names[0] = "Elio";
            names[1] = "Jeshua";
            names[2] = "Jazz";

            Console.WriteLine(names[1]);

            // Arrays Ints
            int[] ages = { 28, 30, 32, 36, 48 };
            Console.WriteLine(ages[0]);

            for (int i = 0; i < ages.Length; i++) 
            {
                Console.WriteLine($"Edad {i+1} = {ages[i]}");           
            }


            // Arrays Multidimensionales
            int[,] matriz = new int[2, 3];

            matriz[0, 0] = 1;
            matriz[0, 1] = 2;
            matriz[0, 2] = 3;
            matriz[1, 0] = 2;
            matriz[1, 1] = 1;
            matriz[1, 2] = 0;

            for (int fila = 0; fila < 2; fila++) 
            {
                for (int colum = 0; colum < 3; colum++) 
                {
                    Console.Write(matriz[fila, colum] + "\t");               
                }
                Console.WriteLine();
            }

        }
    }
}