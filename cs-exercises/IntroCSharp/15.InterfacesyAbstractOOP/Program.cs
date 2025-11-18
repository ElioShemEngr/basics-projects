using System;
using System.Security.Cryptography.X509Certificates;

namespace InterfacesAbstract
{
    class Program
    {
        static void Main()
        {
            // Implementacion de Clases Abstractas
            Empleado e1 = new EmpleadoAsalariado("Ana", 3600);
            Empleado e2 = new EmpleadoPorHoras("Jose", 1000, 40, 20);

            e1.MostrarInformacion();
            Console.WriteLine($"Pago: {e1.CalcularPago()}");

            e2.MostrarInformacion();
            Console.WriteLine($"Pago: {e2.CalcularPago()}");


            // Implementacion de Interfaces
            var calc = new Calculadora();
            calc.Sumar(5, 3);
            calc.Restar(10, 4);
        }
    }

    // Clases Abstractas (No puede ser Instanciada)
    public abstract class Empleado 
    {
        public string Name { get; set; }
        public double Sueldo { get; set; }

        public Empleado(string name, double sueldo) 
        {
            Name = name;
            Sueldo = sueldo;        
        }

        // Método abstracto (debe implementarse en clases hijas)
        public abstract double CalcularPago();

        // Metodo Normal (Opcional)
        public void MostrarInformacion() 
        {
            Console.WriteLine($"Empleado: {Name}, Sueldo Base: {Sueldo}");       
        }
    }

    // Clases derivadas de Abstracts
    // Empleado Asalariado
    public class EmpleadoAsalariado : Empleado 
    {
        public EmpleadoAsalariado(string name, double sueldo)
            : base(name, sueldo) { }

        public override double CalcularPago() 
        {
            return Sueldo;
        }
    }

    // Empleado por horas
    public class EmpleadoPorHoras : Empleado
    {
        public int HorasTrabajadas { get; set; }
        public double PagoPorHora { get; set; }

        public EmpleadoPorHoras(string nombre, double sueldo, int horas, double pago)
            : base(nombre, sueldo)
        {
            HorasTrabajadas = horas;
            PagoPorHora = pago;
        }

        public override double CalcularPago()
        {
            return Sueldo + (HorasTrabajadas * PagoPorHora);
        }
    }


    // Interfaces
    public interface IOperaciones 
    {
        void Sumar(double a, double b);
        void Restar(double a, double b);
    }

    // Clases a partir de interfaces
    public class Calculadora : IOperaciones 
    {
        public void Sumar(double a, double b) 
        {
            Console.WriteLine($"La suma es : {a + b}");        
        }

        public void Restar(double a, double b) 
        {
            Console.WriteLine($"La resta es : {a - b}");
        }
    }

}