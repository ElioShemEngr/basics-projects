using System;

namespace EnumStruct
{
    class Program
    {
        // Enums
        enum TipoArma { Espada, Lanza, Arco, Daga }

        //Structs
        struct DatosArma 
        {
            string nombre;
            int dano;
            TipoArma tipo;

            public DatosArma(string nombre, int dano, TipoArma tipo) 
            {
                this.nombre = nombre;
                this.dano = dano;
                this.tipo = tipo;            
            }

            static void Main()
            {
                TipoArma tipoArma = TipoArma.Arco;
                Console.WriteLine(tipoArma);

                DatosArma arma1 = new DatosArma("Cimitarra de la ira", 28, TipoArma.Espada);
                DatosArma arma2 = new DatosArma("Arco de la guardia", 25, TipoArma.Arco);
            }



        }
    }
}