// Reto 05
// Calculadora Edad

namespace Reto05
{
    class Principal
    {
        public static void CalculadoraEdad()
        {
            int actual = DateTime.Now.Year;
            int nacimiento;

            Console.WriteLine("CALCULADORA DE EDAD");
            Console.Write("Año de Nacimiento > ");

            try
            {
                nacimiento = int.Parse(Console.ReadLine()!);
                Console.WriteLine($"Tu edad es {actual - nacimiento}");

            }
            catch 
            {
                Console.WriteLine($"Ese no es un numero valido");
            }
        }
    }
}

