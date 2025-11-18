using System;
using System.Xml.Linq;

namespace HerenciaPolimorfismo
{
    class Program
    {
        static void Main()
        {
            // Objeto de Clase Original
            var persona1 = new Persona("Elio", 30);
            Console.WriteLine(persona1.Show());

            // Objeto de clase Heredada
            var dev1 = new Dev("ShemDev", 28, "CSharp");
            Console.WriteLine(dev1.Show());

            // Objeto de clase Heredada
            var doctor1 = new Doctor("Beremiz", 42, "Cardiologia");
            Console.WriteLine(doctor1.Show());

        }
    }

    // Clase Persona
    class Persona 
    {
        // Atributos
        protected string name;
        protected int age;

        // Constructor
        public Persona (string name, int age) 
        {
            this.name = name;
            this.age = age;        
        }

        // Metodo
        public virtual string Show() 
        {
            return $"Name : {name} / Age : {age}";
        }
    
    }

    // Clase Dev
    class Dev : Persona
    {
        public string language;
        public Dev(string name, int age, string language) : base(name, age)
        {
            this.language = language;
        }

        // Metodo - Polimorfismo
        public override string Show()
        {
            return $"Name : {name} / Age : {age} / Language : {language}";
        }

    }

    // Clase Doctor
    class Doctor : Persona
    {
        public string speciality;
        public Doctor(string name, int age, string speciality) : base(name, age)
        {
            this.speciality = speciality;
        }

        // Metodo - Polimorfismo
        public override string Show()
        {
            return $"Name : {name} / Age : {age} / Speciality : {speciality}";
        }

    }
}