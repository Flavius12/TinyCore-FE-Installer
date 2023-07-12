import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os

class FinishPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        bitmap = Image.open("res/wizard.png")
        bitmapTk = ImageTk.PhotoImage(bitmap)
        pictureBox2 = tk.Label(self, image=bitmapTk)
        pictureBox2.configure(width=164, height=314)
        pictureBox2.image = bitmapTk
        pictureBox2.pack(anchor="n", expand=False, fill="y", side="left")
        frame14 = ttk.Frame(self)
        frame14.configure(height=200, width=200)
        label10 = ttk.Label(frame14)
        label10.configure(
            font="{Arial} 24 {}",
            text='Installazione completata',
            wraplength=350)
        label10.pack(anchor="w", side="top")
        label11 = ttk.Label(frame14)
        label11.configure(
            text="L'installazione di TinyCore Forensic Edition è stata completata. E' ora possibile rimuovere il disco di installazione. Premendo Fine, il computer verrà riavviato automaticamente.",
            wraplength=400)
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
        #os.system("reboot") #TODO Unlock later
        self.installerApp.quit()

    def onShow(self, params):
        self.installerApp.buttonBack["state"] = "enabled"
        self.installerApp.buttonNext["text"] = "Fine"
        self.installerApp.buttonNext["command"] = lambda : self.onButtonNextClick()
        self.installerApp.buttonCancel["state"] = "disabled"