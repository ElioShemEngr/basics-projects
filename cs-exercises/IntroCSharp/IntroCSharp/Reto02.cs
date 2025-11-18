// Reto 02
// Mensaje por consola
namespace Reto02
{
    class Principal
    {
        public static void Personalizado()
        {
            string name;
            Console.WriteLine("Cual es tu nombre?");
            name = Console.ReadLine();
            Console.WriteLine($"Hola tu nombre es : {name}");
            Console.WriteLine("");

        }
    }
}