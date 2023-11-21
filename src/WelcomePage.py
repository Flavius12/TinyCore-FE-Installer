import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class WelcomePage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        bitmap = Image.open("/usr/local/tcfe-setup/res/wizard.png")
        bitmapTk = ImageTk.PhotoImage(bitmap)
        pictureBox1 = tk.Label(self, image=bitmapTk)
        pictureBox1.configure(width=164, height=314)
        pictureBox1.image = bitmapTk
        pictureBox1.pack(anchor="n", expand=False, fill="y", side="left")
        frame4 = ttk.Frame(self)
        label1 = ttk.Label(frame4)
        label1.configure(
            font="{Arial} 16 {}",
            text="Benvenuto nell'installer di TinyCore Forensic Edition 3.0",
            wraplength=300)
        label1.pack(anchor="w", side="top")
        label2 = ttk.Label(frame4)
        label2.configure(
            text='Il setup ti guiderà nell\'installazione di TinyCore Forensic Edition 3.0, un sistema operativo leggero dedicato all\'analisi forense.\n\nPremi Avanti per continuare.',
            wraplength=300)
        label2.pack(anchor="w", pady=15, side="top")
        frame4.pack(
            anchor="n",
            expand=True,
            fill="both",
            padx=15,
            pady=15,
            side="right")
        self.pack(side="top")

    def onShow(self, params):
        self.installerApp.buttonBack["text"] = "Esci"
        self.installerApp.buttonBack["command"] = lambda : self.installerApp.askQuit()
        self.installerApp.buttonNext["command"] = lambda : self.installerApp.navigateToPage("diskFormatPage")