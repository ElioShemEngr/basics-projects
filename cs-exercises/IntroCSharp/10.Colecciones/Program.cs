using System;
using System.Collections.Generic;

namespace Colecciones
{
    class Program
    {
        static void Main()
        {
            // Colecciones Genericas
            // Listas
            var names = new List<string>();
            names.Add("Elio");
            names.Add("Jeshua");
            names.Add("Jazz");
            names.Remove(names[1]);

            Console.WriteLine(names[1]); // Jazz

            foreach (string name in names) 
            {
                Console.WriteLine($"Alumno : {name}");
            }

            Console.WriteLine(names.Count); // 2

            Console.WriteLine();

            // Diccionarios
            var students = new Dictionary<int, string>();
            students.Add(1, "Lolo");
            students.Add(2, "Pepe");
            students.Add(3, "Tito");
            students.Add(4, "Rigoberto");
            students.Remove(4);

            Console.WriteLine(students[3]);

            foreach (var student in students) 
            {
                Console.WriteLine($"ID: {student.Key} - Nombre: {student.Value}");
            
            }

            Console.WriteLine(students.Count);

        }
    }
}