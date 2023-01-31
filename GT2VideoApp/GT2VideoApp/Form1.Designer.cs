namespace GT2VideoApp
{
    partial class FormMain
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
            this.openFileExcuted = new System.Windows.Forms.OpenFileDialog();
            this.openFileGT = new System.Windows.Forms.OpenFileDialog();
            this.folderBrowserVideos = new System.Windows.Forms.FolderBrowserDialog();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button_videofolder = new System.Windows.Forms.Button();
            this.label_videofolder = new System.Windows.Forms.Label();
            this.textBox_videofolder = new System.Windows.Forms.TextBox();
            this.button_gtfile = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.textBox_gtfile = new System.Windows.Forms.TextBox();
            this.button_filescript = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox_filescript = new System.Windows.Forms.TextBox();
            this.listView1 = new System.Windows.Forms.ListView();
            this.button1 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // openFileExcuted
            // 
            this.openFileExcuted.FileName = "app.py";
            this.openFileExcuted.FileOk += new System.ComponentModel.CancelEventHandler(this.openFileExcuted_FileOk);
            // 
            // openFileGT
            // 
            this.openFileGT.FileName = "gt.txt";
            this.openFileGT.FileOk += new System.ComponentModel.CancelEventHandler(this.openFileGT_FileOk);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.button_videofolder);
            this.groupBox1.Controls.Add(this.label_videofolder);
            this.groupBox1.Controls.Add(this.textBox_videofolder);
            this.groupBox1.Controls.Add(this.button_gtfile);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.textBox_gtfile);
            this.groupBox1.Controls.Add(this.button_filescript);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.textBox_filescript);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBox1.Font = new System.Drawing.Font("Segoe UI", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.groupBox1.Location = new System.Drawing.Point(0, 0);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(598, 157);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Config";
            // 
            // button_videofolder
            // 
            this.button_videofolder.Location = new System.Drawing.Point(511, 82);
            this.button_videofolder.Name = "button_videofolder";
            this.button_videofolder.Size = new System.Drawing.Size(75, 28);
            this.button_videofolder.TabIndex = 8;
            this.button_videofolder.Text = "Browser";
            this.button_videofolder.UseVisualStyleBackColor = true;
            this.button_videofolder.Click += new System.EventHandler(this.button_videofolder_Click);
            // 
            // label_videofolder
            // 
            this.label_videofolder.AutoSize = true;
            this.label_videofolder.Location = new System.Drawing.Point(12, 86);
            this.label_videofolder.Name = "label_videofolder";
            this.label_videofolder.Size = new System.Drawing.Size(87, 17);
            this.label_videofolder.TabIndex = 7;
            this.label_videofolder.Text = "Videos folder";
            // 
            // textBox_videofolder
            // 
            this.textBox_videofolder.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)));
            this.textBox_videofolder.Location = new System.Drawing.Point(101, 83);
            this.textBox_videofolder.Name = "textBox_videofolder";
            this.textBox_videofolder.Size = new System.Drawing.Size(404, 25);
            this.textBox_videofolder.TabIndex = 6;
            // 
            // button_gtfile
            // 
            this.button_gtfile.Location = new System.Drawing.Point(511, 51);
            this.button_gtfile.Name = "button_gtfile";
            this.button_gtfile.Size = new System.Drawing.Size(75, 28);
            this.button_gtfile.TabIndex = 5;
            this.button_gtfile.Text = "Browser";
            this.button_gtfile.UseVisualStyleBackColor = true;
            this.button_gtfile.Click += new System.EventHandler(this.button_gtfile_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 55);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(45, 17);
            this.label2.TabIndex = 4;
            this.label2.Text = "GT file";
            // 
            // textBox_gtfile
            // 
            this.textBox_gtfile.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)));
            this.textBox_gtfile.Location = new System.Drawing.Point(101, 52);
            this.textBox_gtfile.Name = "textBox_gtfile";
            this.textBox_gtfile.Size = new System.Drawing.Size(404, 25);
            this.textBox_gtfile.TabIndex = 3;
            // 
            // button_filescript
            // 
            this.button_filescript.Location = new System.Drawing.Point(511, 20);
            this.button_filescript.Name = "button_filescript";
            this.button_filescript.Size = new System.Drawing.Size(75, 28);
            this.button_filescript.TabIndex = 2;
            this.button_filescript.Text = "Browser";
            this.button_filescript.UseVisualStyleBackColor = true;
            this.button_filescript.Click += new System.EventHandler(this.button_filescript_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(83, 17);
            this.label1.TabIndex = 1;
            this.label1.Text = "Python script";
            // 
            // textBox_filescript
            // 
            this.textBox_filescript.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)));
            this.textBox_filescript.Location = new System.Drawing.Point(101, 21);
            this.textBox_filescript.Name = "textBox_filescript";
            this.textBox_filescript.Size = new System.Drawing.Size(404, 25);
            this.textBox_filescript.TabIndex = 0;
            // 
            // listView1
            // 
            this.listView1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.listView1.Location = new System.Drawing.Point(0, 157);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(598, 306);
            this.listView1.TabIndex = 1;
            this.listView1.UseCompatibleStateImageBehavior = false;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(511, 116);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 35);
            this.button1.TabIndex = 9;
            this.button1.Text = "Load";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // FormMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(598, 463);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.groupBox1);
            this.MaximizeBox = false;
            this.Name = "FormMain";
            this.Text = "GT2Video";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private OpenFileDialog openFileExcuted;
        private OpenFileDialog openFileGT;
        private FolderBrowserDialog folderBrowserVideos;
        private GroupBox groupBox1;
        private ListView listView1;
        private Button button_gtfile;
        private Label label2;
        private TextBox textBox_gtfile;
        private Button button_filescript;
        private Label label1;
        private TextBox textBox_filescript;
        private Button button_videofolder;
        private Label label_videofolder;
        private TextBox textBox_videofolder;
        private Button button1;
    }
}