namespace GT2VideoApp
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
            folderBrowserVideos.InitialDirectory = Application.StartupPath;
        }

        private void button_filescript_Click(object sender, EventArgs e)
        {
            openFileExcuted.ShowDialog();
        }

        private void openFileExcuted_FileOk(object sender, System.ComponentModel.CancelEventArgs e)
        {
            textBox_filescript.Text = openFileExcuted.FileName;
        }

        private void button_gtfile_Click(object sender, EventArgs e)
        {
            openFileGT.ShowDialog();
        }

        private void openFileGT_FileOk(object sender, System.ComponentModel.CancelEventArgs e)
        {
            textBox_gtfile.Text = openFileGT.FileName;  
        }

        private void button_videofolder_Click(object sender, EventArgs e)
        {
            folderBrowserVideos.ShowDialog();
            textBox_videofolder.Text = folderBrowserVideos.SelectedPath;
        }
    }
}