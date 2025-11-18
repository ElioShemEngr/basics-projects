using System;

namespace Operadores
{
    class Program
    {
        static void Main()
        {
            int a = 6;
            int b = 3;
            int c = 2;
            int d = 4;

            // Operadores
            // Operadores Aritmeticos
            Console.WriteLine(a + b);   // Suma (9)
            Console.WriteLine(b - c);   // resta (1)
            Console.WriteLine(b * a);   // Multiplicacion (18)
            Console.WriteLine(a / c);   // Division (3)
            Console.WriteLine(a % d);   // Modulo (2)

            Console.WriteLine();
            // Operadores de Asignacion
            int e;
            e = a + c;
            Console.WriteLine(e);   // (8)
            e += 1;
            Console.WriteLine(e);   // (9)
            e -= 2;
            Console.WriteLine(e);   // (7)
            e *= 2;
            Console.WriteLine(e);   // (14)
            e /= 2;
            Console.WriteLine(e);   // (7)
            e %= 2;
            Console.WriteLine(e);   // (1)


            Console.WriteLine();
            // Operadores Relacionales
            int f = 7;
            Console.WriteLine(f == e);  // False
            Console.WriteLine(a != b);  // True
            Console.WriteLine(d > e);   // True
            Console.WriteLine(b < c);   // False
            Console.WriteLine(f >= a);  // True
            Console.WriteLine(c <= e);  // False

            Console.WriteLine();
            // Operadores Logicos
            int g = 4;
            // Y (&&) -> Ambos deben ser True
            Console.WriteLine(d == g && f != a);    // True
            Console.WriteLine(b == d && a != c);    // False

            // O (||) -> Al menos uno debe ser True
            Console.WriteLine(d > e || b < c);      // True
            Console.WriteLine(c <= e || b < c);     // False

            // Not (!)
            Console.WriteLine(!(f == e));   // True
            Console.WriteLine(!(a != b));   // False

        }
    }
}