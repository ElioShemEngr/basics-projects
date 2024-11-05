namespace MyfirstApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        double numero1;
        double numero2;
        double resultado;

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btn_suma_Click(object sender, EventArgs e)
        {
            Suma();
        }

        //Metodo de suma
        private void Suma() 
        {
            try
            {
                numero1 = Convert.ToDouble(txtB_numero1.Text);
                numero2 = Convert.ToDouble(txtB_numero2.Text);
                resultado = numero1 + numero2;
                lbl_resultadoTotal.Text = Convert.ToString(resultado);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btn_resta_Click(object sender, EventArgs e)
        {
            Resta();
        }

        //Metodo de Resta
        private void Resta()
        {
            try
            {
                numero1 = Convert.ToDouble(txtB_numero1.Text);
                numero2 = Convert.ToDouble(txtB_numero2.Text);
                resultado = numero1 - numero2;
                lbl_resultadoTotal.Text = Convert.ToString(resultado);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btn_mult_Click(object sender, EventArgs e)
        {
            Multiplicar();
        }

        //Metodo de Multiplicar
        private void Multiplicar()
        {
            try
            {
                numero1 = Convert.ToDouble(txtB_numero1.Text);
                numero2 = Convert.ToDouble(txtB_numero2.Text);
                resultado = numero1 * numero2;
                lbl_resultadoTotal.Text = Convert.ToString(resultado);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btn_div_Click(object sender, EventArgs e)
        {
            Dividir();
        }

        //Metodo de Dividir
        private void Dividir()
        {
            try
            {
                numero1 = Convert.ToDouble(txtB_numero1.Text);
                numero2 = Convert.ToDouble(txtB_numero2.Text);
                resultado = numero1 / numero2;
                lbl_resultadoTotal.Text = resultado.ToString("F2");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

    }
}
