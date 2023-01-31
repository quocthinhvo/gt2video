namespace GT2VideoApp
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
        }

        private void button_filescript_Click(object sender, EventArgs e)
        {
            openFileExcuted.ShowDialog();
        }

        private void openFileExcuted_FileOk(object sender, System.ComponentModel.CancelEventArgs e)
        {
            textBox_filescript.Text = openFileExcuted.FileName;
        }
    }
}