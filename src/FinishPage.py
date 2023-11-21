import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os

class FinishPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        bitmap = Image.open("/usr/local/tcfe-setup/res/wizard.png")
        bitmapTk = ImageTk.PhotoImage(bitmap)
        pictureBox2 = tk.Label(self, image=bitmapTk)
        pictureBox2.configure(width=164, height=314)
        pictureBox2.image = bitmapTk
        pictureBox2.pack(anchor="n", expand=False, fill="y", side="left")
        frame14 = ttk.Frame(self)
        frame14.configure(height=200, width=200)
        label10 = ttk.Label(frame14)
        label10.configure(
            font="{Arial} 16 {}",
            text='Installazione completata',
            wraplength=300)
        label10.pack(anchor="w", side="top")
        label11 = ttk.Label(frame14)
        label11.configure(
            text="L'installazione di TinyCore Forensic Edition è stata completata.\n\nE' ora possibile rimuovere il disco di installazione. Premendo Fine, il computer verrà riavviato automaticamente.",
            wraplength=300)
        label11.pack(anchor="w", pady=15, side="top")
        frame14.pack(
            anchor="n",
            expand=True,
            fill="both",
            padx=15,
            pady=15,
            side="right")
        self.pack(side="top")

    def onButtonNextClick(self):
        self.installerApp.quit(0)

    def onShow(self, params):
        self.installerApp.buttonBack["state"] = "disabled"
        self.installerApp.buttonNext["text"] = "Fine"
        self.installerApp.buttonNext["state"] = "enabled"
        self.installerApp.buttonNext["command"] = lambda : self.onButtonNextClick()
        self.installerApp.buttonCancel["state"] = "disabled"