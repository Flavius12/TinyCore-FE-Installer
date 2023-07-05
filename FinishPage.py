import tkinter as tk
import tkinter.ttk as ttk
import os

class FinishPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        canvas2 = tk.Canvas(self)
        canvas2.configure(width=240)
        canvas2.pack(anchor="n", expand=False, fill="y", side="left")
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
            text="L'installazione di TinyCore Forensics Edition è stata completata. E' ora possibile riavviare il computer.",
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
        self.installerApp.buttonBack["state"] = "disabled"
        self.installerApp.buttonNext["text"] = "Fine"
        self.installerApp.buttonNext["command"] = lambda : self.onButtonNextClick()
        self.installerApp.buttonCancel["state"] = "disabled"