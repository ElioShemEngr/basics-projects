// Reto 06
// Par o Impar

namespace Reto06 
{
    class Principal 
    {
        public static void ParImpar() 
        {

            Console.WriteLine("PAR O IMPAR");
            Console.Write("Ingrese Numero > ");

            if (int.TryParse(Console.ReadLine(), out int num1))
            {
                if ((num1 % 2 == 0))
                {
                    Console.WriteLine($"El numero {num1} es par");
                }
                else
                {
                    Console.WriteLine($"El numero {num1} es impar");
                }
            }
            else 
            {
                Console.WriteLine($"Ingrese un numero...");
            }
            
        } 
    
    }

}