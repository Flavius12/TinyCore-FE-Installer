import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class WelcomePage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        canvas1 = tk.Canvas(self)
        canvas1.configure(width=240)
        canvas1.pack(anchor="n", expand=False, fill="y", side="left")
        frame4 = ttk.Frame(self)
        frame4.configure(height=200, width=200)
        label1 = ttk.Label(frame4)
        label1.configure(
            font="{Arial} 24 {}",
            text="Benvenuto nell'installer di TinyCore Forensic Edition 1.0",
            wraplength=350)
        label1.pack(anchor="w", side="top")
        label2 = ttk.Label(frame4)
        label2.configure(
            text='Seguendo questo installer potreai installare tinyCore...')
        label2.pack(anchor="w", pady=15, side="top")
        frame4.pack(
            anchor="n",
            expand=True,
            fill="both",
            padx=15,
            pady=15,
            side="right")
        self.pack(side="top")

    def onShow(self):
        self.installerApp.buttonBack["text"] = "Esci"
        self.installerApp.buttonBack["command"] = lambda : self.installerApp.askQuit()
        self.installerApp.buttonNext["command"] = lambda : self.installerApp.navigateToPage("diskFormatPage")