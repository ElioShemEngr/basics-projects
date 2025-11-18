// Reto 03
// Suma de Numeros
namespace Reto03
{
    class Principal
    {
        public static void SumaNumeros()
        {
            int num1, num2;

            Console.WriteLine("SUMA DE 02 NUMEROS : ");

            Console.Write("Indique Primer valor > ");
            num1 = int.Parse(Console.ReadLine()!);

            Console.Write("Indique segundo valor > ");
            num2 = int.Parse(Console.ReadLine()!);

            Console.WriteLine($"El resultado de la suma es : {num1 + num2}");

        }
    }
}