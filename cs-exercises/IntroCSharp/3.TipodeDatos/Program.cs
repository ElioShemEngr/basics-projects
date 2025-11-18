using System; 

namespace TiposdeDatos
{
    class Program 
    {
        static void Main() 
        {
            // Tipos de Datos
            // Declaracion Explicita (Recomendada)
            string name = "Elioshem";   // Cadena de Caracteres
            int age = 30;               // Numeros Enteros
            double height = 1.78;       // Numeros Decimales
            bool student = true;        // True o False

            Console.WriteLine(name);
            Console.WriteLine(age);
            Console.WriteLine(height);
            Console.WriteLine(student);

            // Inferencia de Tipos
            var name1 = "Luis";         // Cadena de Caracteres
            var age1 = 25;              // Numeros Enteros
            var height1 = 1.65;         // Numeros Decimales
            var student1 = false;       // True o False

            Console.WriteLine(name1);
            Console.WriteLine(age1);
            Console.WriteLine(height1);
            Console.WriteLine(student1);

        }
    }
}