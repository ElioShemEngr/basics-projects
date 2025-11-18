// Reto 04
// Simple Login

namespace Reto04
{
    class Principal
    {
        public static void SimpleLogin()
        {
            
            string user, password;

            Console.WriteLine("SIMPLE LOGIN");

            Console.Write("UserID > ");
            user = Console.ReadLine();
            Console.Write("Password > ");
            password = Console.ReadLine();

            if (user == "Elioshem" && password == "Xai9kzcm")
            {
                Console.WriteLine($"WELCOME {user}...!!");
            }
            else if (user == "" || password == "") 
            {
                Console.WriteLine("Datos Incompletos..!!");            
            }
            else {
                Console.WriteLine($"User or Password INCORRECT!!");
            }

        }
    }
}

