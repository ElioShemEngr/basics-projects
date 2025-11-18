using System;

namespace ClasesObjetos
{
    class Program 
    {
        static void Main() 
        {
            var sale1 = new Sale(32, DateTime.Now);
            Console.WriteLine(sale1.GetInfo());
        }
    }

    class Sale 
    {
        int total;
        DateTime date;

        public Sale(int total, DateTime date) 
        {
            this.total = total;
            this.date = date;
        
        }

        public string GetInfo()
        {
            return $"Total : {total} / Fecha : {date.ToLongDateString()}";
        }

        public void Show() 
        {
            Console.WriteLine("Hola soy una venta");
        }
    }
}