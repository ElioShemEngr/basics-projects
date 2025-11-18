using System;

namespace PropsDelegaEvents
{
    class Program
    {
        static void Main()
        {
            Usuario user01 = new Usuario("Elioshem", "engr@micorreo.com");
            Console.WriteLine(user01.Nombre);
            // Console.WriteLine(user01.Correo); -> Error ya que no esta habilitado el get

            // LLamada a Delegates
            Calculadora c = new Calculadora();
            Operacion op = c.Sumar;
            op(5, 3);
        }

    }

    // Clases usando propiedades
    public class Usuario
    {
        public string Nombre { get; }
        public string Correo { private get; set; }

        public Usuario(string nombre, string correo)
        {
            Nombre = nombre;
            Correo = correo;
        }
    }


    // Delegates
    public delegate void Operacion(int x, int y);

    public class Calculadora
    {
        public void Sumar(int a, int b)
        {
            Console.WriteLine($"Resultado: {a + b}");
        }
    }
}
