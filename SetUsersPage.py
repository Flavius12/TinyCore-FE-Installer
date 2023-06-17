import tkinter as tk
import tkinter.ttk as ttk

class SetUsersPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        frame22 = ttk.Frame(self)
        frame22.configure(height=50, width=200)
        frame23 = ttk.Frame(frame22)
        frame23.configure(height=200, width=200)
        canvas6 = tk.Canvas(frame23)
        canvas6.configure(height=50, width=100)
        canvas6.pack(expand=False, fill="y", side="left")
        label16 = ttk.Label(frame23)
        label16.configure(font="{Arial} 14 {bold}", text='Impostazione utente')
        label16.pack(anchor="w", padx=20, pady=5, side="top")
        label17 = ttk.Label(frame23)
        label17.configure(text="Imposta l'utente di sistema")
        label17.pack(anchor="w", padx=20, side="top")
        frame23.pack(expand=True, fill="both", side="top")
        separator2 = ttk.Separator(frame22)
        separator2.configure(orient="horizontal")
        separator2.pack(anchor="s", expand=True, fill="x", side="bottom")
        frame22.pack(expand=False, fill="x", side="top")
        frame24 = ttk.Frame(self)
        frame24.configure(height=200, width=200)
        label19 = ttk.Label(frame24)
        label19.configure(
            text="Imposta il nome utente per l'account. Il nome utente deve contenere esclusivamente lettere minuscole e/o numeri.",
            wraplength=500)
        label19.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        label25 = ttk.Label(frame24)
        label25.configure(text='Nome utente:')
        label25.pack(anchor="w", padx=75, side="top")
        entry6 = ttk.Entry(frame24)
        entry6.pack(anchor="w", fill="x", padx=75, pady=10, side="top")
        label26 = ttk.Label(frame24)
        label26.configure(
            text="Imposta una password sicura per l'account. La password deve avere minimo 8 caratteri e contenere...",
            wraplength=500)
        label26.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        label27 = ttk.Label(frame24)
        label27.configure(text='Password:')
        label27.pack(anchor="w", padx=75, side="top")
        entry7 = ttk.Entry(frame24)
        entry7.pack(anchor="w", fill="x", padx=75, pady=10, side="top")
        label28 = ttk.Label(frame24)
        label28.configure(text='Conferma password:')
        label28.pack(anchor="w", padx=75, side="top")
        entry8 = ttk.Entry(frame24)
        entry8.pack(anchor="w", fill="x", padx=75, pady=10, side="top")
        checkbutton1 = ttk.Checkbutton(frame24)
        checkbutton1.configure(text='Mostra password')
        checkbutton1.pack(anchor="w", padx=75, side="top")
        frame24.pack(expand=True, fill="both", side="top")
        self.pack(side="top")

    def onShow(self, params):
        self.installerApp.buttonBack["state"] = "disabled"
        self.installerApp.buttonNext["state"] = "enabled"
        self.installerApp.buttonNext["command"] = lambda : self.installerApp.navigateToPage("finishPage")
        self.installerApp.buttonCancel["state"] = "disabled"