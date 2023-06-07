import tkinter as tk
import tkinter.ttk as ttk

class InstallPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        frame10 = ttk.Frame(self)
        frame10.configure(height=50, width=200)
        frame11 = ttk.Frame(frame10)
        frame11.configure(height=200, width=200)
        canvas4 = tk.Canvas(frame11)
        canvas4.configure(height=50, width=100)
        canvas4.pack(expand=False, fill="y", side="left")
        label7 = ttk.Label(frame11)
        label7.configure(font="{Arial} 14 {bold}", text='Installazione')
        label7.pack(anchor="w", padx=20, pady=5, side="top")
        label8 = ttk.Label(frame11)
        label8.configure(text='Installazione in corso...')
        label8.pack(anchor="w", padx=20, side="top")
        frame11.pack(expand=True, fill="both", side="top")
        separator5 = ttk.Separator(frame10)
        separator5.configure(orient="horizontal")
        separator5.pack(anchor="s", expand=True, fill="x", side="bottom")
        frame10.pack(expand=False, fill="x", side="top")
        frame12 = ttk.Frame(self)
        frame12.configure(height=200, width=200)
        label9 = ttk.Label(frame12)
        label9.configure(text='Installazione di libcurl.so...')
        label9.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        progressbar2 = ttk.Progressbar(frame12)
        progressbar2.configure(orient="horizontal", value=20)
        progressbar2.pack(fill="x", padx=50, side="top")
        frame12.pack(expand=True, fill="both", side="top")
        self.pack(side="top")

    def onShow(self):
        self.installerApp.buttonBack["state"] = "disabled"
        self.installerApp.buttonNext["state"] = "disabled"
        self.installerApp.buttonCancel["state"] = "disabled"
        self.installerApp.navigateToPage("setUsersPage")
