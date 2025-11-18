using System;
using System.Security.Principal;

namespace ErrorHandlig 
{
    class Program
    {
        static void Main() 
        {
            try
            {
                int x = 5;
                Console.WriteLine($"{x / 0}");
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Error: división por cero");
            }
            finally
            {
                Console.WriteLine("Siempre se ejecuta");
            }
        }
     }
}