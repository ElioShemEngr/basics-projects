using System;

namespace Funciones
{
    class Program
    {
        static void Main()
        {
            // Funciones con retorno (return)
            // Ejemplo string
            string Saludo(string name)
            {
                return $"Hola mi nombre es {name}";
            }

            string saludoUser = Saludo("Elioshem");
            Console.WriteLine(saludoUser);

            Console.WriteLine();

            // Ejemplo int
            int Sumar(int num1, int num2) 
            {
                return num1 + num2;
            }

            int resultado = Sumar(5, 7);
            Console.WriteLine(resultado);

            Console.WriteLine();

            // Ejemplo double
            double AreaRectangulo(double b, double h) 
            {
                return (b + h) / 2;            
            }

            double area = AreaRectangulo(10.50, 22.80);
            Console.WriteLine(area);

            Console.WriteLine();

            // Funciones sin retorno (void)
            void HolaMundo() 
            {
                Console.WriteLine("Hola Mundo desde C#");            
            }

            HolaMundo();


            // Parametros Predeterminados
            int Promedio(int nota1, int nota2, int nota3 = 10) 
            {
                return (nota1 + nota2 + nota3) / 3;          
            }

            int notaFinal = Promedio(15, 12);
            Console.WriteLine(notaFinal);
        }

    }

}