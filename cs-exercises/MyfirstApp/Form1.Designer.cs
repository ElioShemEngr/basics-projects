namespace MyfirstApp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lbl_numero1 = new Label();
            txtB_numero1 = new TextBox();
            panel1 = new Panel();
            lbl_numero2 = new Label();
            txtB_numero2 = new TextBox();
            panel2 = new Panel();
            btn_suma = new Button();
            lbl_resultado = new Label();
            btn_resta = new Button();
            btn_mult = new Button();
            btn_div = new Button();
            lbl_resultadoTotal = new Label();
            SuspendLayout();
            // 
            // lbl_numero1
            // 
            lbl_numero1.AutoSize = true;
            lbl_numero1.Location = new Point(74, 53);
            lbl_numero1.Margin = new Padding(4, 0, 4, 0);
            lbl_numero1.Name = "lbl_numero1";
            lbl_numero1.Size = new Size(100, 22);
            lbl_numero1.TabIndex = 0;
            lbl_numero1.Text = "Numero 1:";
            // 
            // txtB_numero1
            // 
            txtB_numero1.BackColor = Color.FromArgb(29, 29, 29);
            txtB_numero1.BorderStyle = BorderStyle.None;
            txtB_numero1.ForeColor = Color.White;
            txtB_numero1.Location = new Point(181, 50);
            txtB_numero1.Name = "txtB_numero1";
            txtB_numero1.Size = new Size(200, 22);
            txtB_numero1.TabIndex = 1;
            // 
            // panel1
            // 
            panel1.BackColor = Color.White;
            panel1.Location = new Point(181, 78);
            panel1.Name = "panel1";
            panel1.Size = new Size(200, 2);
            panel1.TabIndex = 2;
            // 
            // lbl_numero2
            // 
            lbl_numero2.AutoSize = true;
            lbl_numero2.Location = new Point(74, 115);
            lbl_numero2.Margin = new Padding(4, 0, 4, 0);
            lbl_numero2.Name = "lbl_numero2";
            lbl_numero2.Size = new Size(100, 22);
            lbl_numero2.TabIndex = 0;
            lbl_numero2.Text = "Numero 2:";
            // 
            // txtB_numero2
            // 
            txtB_numero2.BackColor = Color.FromArgb(29, 29, 29);
            txtB_numero2.BorderStyle = BorderStyle.None;
            txtB_numero2.ForeColor = Color.White;
            txtB_numero2.Location = new Point(181, 112);
            txtB_numero2.Name = "txtB_numero2";
            txtB_numero2.Size = new Size(200, 22);
            txtB_numero2.TabIndex = 1;
            // 
            // panel2
            // 
            panel2.BackColor = Color.White;
            panel2.Location = new Point(181, 140);
            panel2.Name = "panel2";
            panel2.Size = new Size(200, 2);
            panel2.TabIndex = 2;
            // 
            // btn_suma
            // 
            btn_suma.Font = new Font("Consolas", 18F, FontStyle.Bold);
            btn_suma.ForeColor = Color.FromArgb(29, 29, 29);
            btn_suma.Location = new Point(98, 185);
            btn_suma.Name = "btn_suma";
            btn_suma.Size = new Size(45, 45);
            btn_suma.TabIndex = 3;
            btn_suma.Text = "+";
            btn_suma.UseVisualStyleBackColor = true;
            btn_suma.Click += btn_suma_Click;
            // 
            // lbl_resultado
            // 
            lbl_resultado.AutoSize = true;
            lbl_resultado.Location = new Point(74, 263);
            lbl_resultado.Margin = new Padding(4, 0, 4, 0);
            lbl_resultado.Name = "lbl_resultado";
            lbl_resultado.Size = new Size(110, 22);
            lbl_resultado.TabIndex = 0;
            lbl_resultado.Text = "Resultado:";
            // 
            // btn_resta
            // 
            btn_resta.Font = new Font("Consolas", 18F, FontStyle.Bold);
            btn_resta.ForeColor = Color.FromArgb(29, 29, 29);
            btn_resta.Location = new Point(168, 185);
            btn_resta.Name = "btn_resta";
            btn_resta.Size = new Size(45, 45);
            btn_resta.TabIndex = 3;
            btn_resta.Text = "-";
            btn_resta.UseVisualStyleBackColor = true;
            btn_resta.Click += btn_resta_Click;
            // 
            // btn_mult
            // 
            btn_mult.Font = new Font("Consolas", 18F, FontStyle.Bold);
            btn_mult.ForeColor = Color.FromArgb(29, 29, 29);
            btn_mult.Location = new Point(239, 185);
            btn_mult.Name = "btn_mult";
            btn_mult.Size = new Size(45, 45);
            btn_mult.TabIndex = 3;
            btn_mult.Text = "x";
            btn_mult.UseVisualStyleBackColor = true;
            btn_mult.Click += btn_mult_Click;
            // 
            // btn_div
            // 
            btn_div.Font = new Font("Consolas", 18F, FontStyle.Bold);
            btn_div.ForeColor = Color.FromArgb(29, 29, 29);
            btn_div.Location = new Point(312, 185);
            btn_div.Name = "btn_div";
            btn_div.Size = new Size(45, 45);
            btn_div.TabIndex = 3;
            btn_div.Text = "÷";
            btn_div.UseVisualStyleBackColor = true;
            btn_div.Click += btn_div_Click;
            // 
            // lbl_resultadoTotal
            // 
            lbl_resultadoTotal.AutoSize = true;
            lbl_resultadoTotal.Location = new Point(181, 263);
            lbl_resultadoTotal.Margin = new Padding(4, 0, 4, 0);
            lbl_resultadoTotal.Name = "lbl_resultadoTotal";
            lbl_resultadoTotal.Size = new Size(20, 22);
            lbl_resultadoTotal.TabIndex = 0;
            lbl_resultadoTotal.Text = "-";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.FromArgb(29, 29, 29);
            ClientSize = new Size(484, 661);
            Controls.Add(btn_div);
            Controls.Add(btn_mult);
            Controls.Add(btn_resta);
            Controls.Add(btn_suma);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Controls.Add(txtB_numero2);
            Controls.Add(txtB_numero1);
            Controls.Add(lbl_resultadoTotal);
            Controls.Add(lbl_resultado);
            Controls.Add(lbl_numero2);
            Controls.Add(lbl_numero1);
            Font = new Font("Consolas", 14F);
            ForeColor = Color.White;
            Margin = new Padding(4, 5, 4, 5);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lbl_numero1;
        private TextBox txtB_numero1;
        private Panel panel1;
        private Label lbl_numero2;
        private TextBox txtB_numero2;
        private Panel panel2;
        private Button btn_suma;
        private Label lbl_resultado;
        private Button btn_resta;
        private Button btn_mult;
        private Button btn_div;
        private Label lbl_resultadoTotal;
    }
}
