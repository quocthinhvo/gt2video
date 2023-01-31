using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;
using System.Diagnostics;
using System;

namespace GT2VideoApp
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
            //folderBrowserVideos.InitialDirectory = Application.StartupPath;
            openFileExcuted.InitialDirectory = Application.StartupPath; 
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

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox_videofolder.Text != "")
            {

                String[] files = Directory.GetFiles(textBox_videofolder.Text);

                for (int i = 0; i < files.Length; i++)
                {
                    FileInfo file = new FileInfo(files[i]);
                    ListViewItem item = new ListViewItem();
                    item.Text = file.FullName;
                    listView1.Items.Add(item);
                }
            } 
            else
            {
                MessageBox.Show("An occured error", "Please choose videos path", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void FormMain_Load(object sender, EventArgs e)
        {
            ColumnHeader header = new ColumnHeader();
            header.Text = "List videos: ";
            header.Name = "col1";
            listView1.Columns.Add(header);
            listView1.Columns[0].Width = -2;
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
    
        }

        private void listView1_ItemActivate(object sender, EventArgs e)
        {
            string command = "/C python " +  textBox_filescript.Text + " " + textBox_gtfile.Text +" " + listView1.SelectedItems[0].Text;
            Process p = new Process();
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.Arguments = command;
            p.Start();
            p.WaitForExit();

        }
    }
}