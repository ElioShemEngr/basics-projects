// Conceptos de Programacion Orientada a Objetos

namespace POO
{
    class Program
    {
        static void Main()
        {
            var product1 = new Product(1, "Pilsen", 10);
            var product2 = new Product(2, "Cusquena", 8);
            var product3 = new Product(3, "San Juan", 6);


            var client1 = new Customer(1, "Felipe");
            var client2 = new Customer(2, "Pepe");

            var sale1 = new Sale(1, client1);
            sale1.AddConcept(product1, 6);
            sale1.AddConcept(product3, 3);
            
            Console.WriteLine($"La fecha de venta es : {sale1.Date}");
            Console.WriteLine($"El total de la venta es : {sale1.Total}");


            sale1.CreateInvoice();

            Console.Read();
        }
    }

    public class Product 
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
        
        public Product (int id, string name, decimal price)
        {
            this.Id = id;
            this.Name = name;
            this.Price = price;
        }
    }

    public class Customer
    {
        public int ID { get; set; }
        public string Name { get; set; }

        public Customer (int id, string name) 
        {
            this.ID = id;
            this.Name = name;
        }
    }

    public class Concept 
    {
        public Product Product { get; set; }
        public int Quantity { get; set; }

        public Concept(Product product, int quantity) 
        {
            this.Product = product;
            this.Quantity = quantity;
        }

        public decimal Subtotal 
        { 
            get 
            {
                return Product.Price* Quantity;
            } 
        }
    }

    public class Sale 
    {
        public int ID { get; set; }
        public Customer Customer { get; set; }
        public List<Concept> Concepts { get; set; }
        public DateTime Date { get; set; }

        private Invoice _invoice;
        private Send _send;

        public decimal Total 
        {
            get 
            {
                decimal total = 0;
                foreach (Concept concept in Concepts) 
                {
                    total += concept.Subtotal;
                
                }
                return total;
            }        
        }

        public Sale(int id, Customer customer, Invoice invoice, Send send) 
        {
            this.ID = id;
            this.Customer = customer;
            this.Concepts = new List<Concept>();
            this.Date = DateTime.Now;
            this._invoice = invoice;
            this._send = send;
        }

        public void AddConcept(Product product, int quantity) 
        {
            Concepts.Add(new Concept(product, quantity));                   
        }

        public void CreateInvoice() 
        {
            _invoice.Create();
            _send.Send("Se envia la factura");
        }
    }

    public interface Invoice 
    {
        public void Create();
    }

    public interface Send
    {
        public void Send(string content);  
    
    }
}