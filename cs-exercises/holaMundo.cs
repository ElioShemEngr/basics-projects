using System;
using System.Collections.Generic;

namespace CSharpHolaMundo
{
    class HolaMundo
    {
        static int Sumar(int a, int b)
        {
            return a + b;
        }

        static void Main()
        {
            int resultado = Sumar(5, 7);
            Console.WriteLine($"El resultado de la suma es : {resultado}");

            
            Console.WriteLine("Hola, C#");

            //Esto es un comentario en una linea

            /*
            Este es un comentario
            creado en varias
            lineas            
            */

            //Tipos de datos (Comunes o Primitivos)
            string myString = "Elioshem";
            Console.WriteLine(myString);

            int myInt = 7;
            myInt = 10;
            Console.WriteLine(myInt);
            Console.WriteLine(myInt + 5);
            myInt = myInt - 8;
            Console.WriteLine(myInt);

            double myDouble = 3.14;
            Console.WriteLine(myDouble);

            Console.WriteLine(myInt * myDouble);

            bool myBool = true;
            Console.WriteLine(myBool);

            //Tipos de datos (No Comunes)
            float myFloat = 5.25f;
            Console.WriteLine(myFloat);
        
            var myString2 = "Cardenas";
            myString2 = "11";
            Console.WriteLine(myString2);

            dynamic myDynamic = 22;
            myDynamic = "Hola";
            Console.WriteLine(myDynamic);

            const double Pi = 3.14;
            //Pi = 6.57; -> Error!
            Console.WriteLine(Pi);

            //Concatenaciones y Formateo
            Console.WriteLine($"Mi nombre es : {myString}");
            Console.WriteLine($"El resultado de la suma es : {myInt + myFloat}");

            //Estructuras de Control

            //Condicionales
            int edad = 16;

            if(edad >= 18)
            {
                Console.WriteLine("Es mayor de edad");
            }
            else if(edad == 16)
            {
                Console.WriteLine("Es graduado");
            }
            else
            {
                Console.WriteLine("Es menor de edad");
            }

            //Switch
            int dia = 4;

            switch(dia)
            {
                case 1:
                    Console.WriteLine("Domingo");
                    break;
                case 2:
                    Console.WriteLine("Lunes");
                    break;
                case 3:
                    Console.WriteLine("Martes");
                    break;
                case 4:
                    Console.WriteLine("Miercoles");
                    break;
                case 5:
                    Console.WriteLine("Jueves");
                    break;
                case 6:
                    Console.WriteLine("Viernes");
                    break;
                case 7:
                    Console.WriteLine("Sabado");
                    break;
                default:
                    Console.WriteLine("Dia no valido");
                    break;
            }

            //Bucles

            //for
            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine("El valor es : " + i);
            }

            //while
            int contador = 1;
            while (contador <= 3)
            {
                Console.WriteLine(contador);
                contador++;
            }

            //Colecciones y Arreglos

            //Arreglos o Arrays
            var myArray = new int[5] {11, 22, 33, 44, 55};
            
            myArray[2] = 77;
            //Acceso a los elementos de un arreglo
            Console.WriteLine(myArray[1]);
            Console.WriteLine(myArray[3]);

            //Recorrer arreglos con un bucle
            for (int i = 0; i < myArray.Length; i++)
            {
                Console.WriteLine(myArray[i]);
            }

            //Listas
            var nombres = new List<string>();
            //Agregar elementos a una lista
            nombres.Add("Ana");
            nombres.Add("Luis");
            nombres.Add("Carlos");
            //Acceso a los elementos de una lista
            Console.WriteLine(nombres[1]);

            //Recorre la lista con un foreach
            foreach(string nombre in nombres)
            {
                Console.WriteLine(nombre);
            }

            //Diccionarios
            var edades = new Dictionary<string, int>();
            //Agregar elementos a un diccionario
            edades["Ana"] = 25;
            edades["Luis"] = 30;
            edades["Carlos"] = 20;
            //Acceso a los elementos de un diccionario
            Console.WriteLine(edades["Luis"]);

            //Recorre el diccionario con un foreach
            foreach(var par in edades)
            {
                Console.WriteLine($"{par.Key}: {par.Value}");
            }

        }
    }
}
