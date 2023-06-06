import tkinter as tk
import tkinter.ttk as ttk


class InstallerApp:
    def __init__(self):
        # build ui
        mainWindow = tk.Tk()
        mainWindow.configure(background="lightgray", height=480, width=640)
        mainWindow.title("Installer")
        # Configure Styles
        style = ttk.Style()
        style.layout('Tabless.TNotebook.Tab', []) # turn off tabs
        style.configure('Tabless.TNotebook', borderwidth=0) # Flat style
        notebook1 = ttk.Notebook(mainWindow, style="Tabless.TNotebook")
        notebook1.configure(height=480, width=640)
        self.welcomePage = WelcomePage(notebook1)
        notebook1.add(self.welcomePage, text='tab1')
        frame16 = ttk.Frame(notebook1)
        frame16.configure(height=200, width=200)
        frame17 = ttk.Frame(frame16)
        frame17.configure(height=50, width=200)
        frame18 = ttk.Frame(frame17)
        frame18.configure(height=200, width=200)
        canvas5 = tk.Canvas(frame18)
        canvas5.configure(height=50, width=100)
        canvas5.pack(expand=False, fill="y", side="left")
        label12 = ttk.Label(frame18)
        label12.configure(
            font="{Arial} 14 {bold}",
            text='Formattazione dischi')
        label12.pack(anchor="w", padx=20, pady=5, side="top")
        label13 = ttk.Label(frame18)
        label13.configure(text='Formatta i dischi rigidi')
        label13.pack(anchor="w", padx=20, side="top")
        frame18.pack(expand=True, fill="both", side="top")
        separator1 = ttk.Separator(frame17)
        separator1.configure(orient="horizontal")
        separator1.pack(anchor="s", expand=True, fill="x", side="bottom")
        frame17.pack(expand=False, fill="x", side="top")
        frame19 = ttk.Frame(frame16)
        frame19.configure(height=200, width=200)
        label14 = ttk.Label(frame19)
        label14.configure(
            text='Seleziona il metodo di partizionamento del disco:')
        label14.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        radiobutton1 = ttk.Radiobutton(frame19)
        radiobutton1.configure(text='Automatico (usa intero disco)')
        radiobutton1.pack(anchor="w", padx=75, pady=5, side="top")
        radiobutton3 = ttk.Radiobutton(frame19)
        radiobutton3.configure(text='Manuale')
        radiobutton3.pack(anchor="w", padx=75, pady=5, side="top")
        frame19.pack(expand=True, fill="both", side="top")
        frame16.pack(side="top")
        notebook1.add(frame16, text='tab2')
        frame2 = ttk.Frame(notebook1)
        frame2.configure(height=200, width=200)
        frame5 = ttk.Frame(frame2)
        frame5.configure(height=50, width=200)
        frame7 = ttk.Frame(frame5)
        frame7.configure(height=200, width=200)
        canvas3 = tk.Canvas(frame7)
        canvas3.configure(height=50, width=100)
        canvas3.pack(expand=False, fill="y", side="left")
        label3 = ttk.Label(frame7)
        label3.configure(font="{Arial} 14 {bold}", text='Formattazione dischi')
        label3.pack(anchor="w", padx=20, pady=5, side="top")
        label4 = ttk.Label(frame7)
        label4.configure(text='Formatta i dischi rigidi')
        label4.pack(anchor="w", padx=20, side="top")
        frame7.pack(expand=True, fill="both", side="top")
        separator3 = ttk.Separator(frame5)
        separator3.configure(orient="horizontal")
        separator3.pack(anchor="s", expand=True, fill="x", side="bottom")
        frame5.pack(expand=False, fill="x", side="top")
        frame6 = ttk.Frame(frame2)
        frame6.configure(height=200, width=200)
        label5 = ttk.Label(frame6)
        label5.configure(
            text='Seleziona il disco rigido dove installare TinyCore Forensics Edition:')
        label5.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        treeview1 = ttk.Treeview(frame6)
        treeview1.configure(selectmode="extended")
        treeview1.pack(expand=False, fill="x", padx=50, side="top")
        frame15 = ttk.Frame(frame6)
        frame15.configure(height=200, width=200)
        button8 = ttk.Button(frame15)
        button8.configure(text='Nuova partizione...')
        button8.pack(side="left")
        button9 = ttk.Button(frame15)
        button9.configure(text='Formatta...')
        button9.pack(side="left")
        button10 = ttk.Button(frame15)
        button10.configure(text='Elimina...')
        button10.pack(side="left")
        frame15.pack(anchor="w", padx=50, pady=10, side="top")
        frame6.pack(expand=True, fill="both", side="top")
        frame2.pack(side="top")
        notebook1.add(frame2, text='tab2')
        frame9 = ttk.Frame(notebook1)
        frame9.configure(height=200, width=200)
        frame10 = ttk.Frame(frame9)
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
        frame12 = ttk.Frame(frame9)
        frame12.configure(height=200, width=200)
        label9 = ttk.Label(frame12)
        label9.configure(text='Installazione di libcurl.so...')
        label9.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        progressbar2 = ttk.Progressbar(frame12)
        progressbar2.configure(orient="horizontal", value=20)
        progressbar2.pack(fill="x", padx=50, side="top")
        frame12.pack(expand=True, fill="both", side="top")
        frame9.pack(side="top")
        notebook1.add(frame9, text='tab2')
        frame21 = ttk.Frame(notebook1)
        frame21.configure(height=200, width=200)
        frame22 = ttk.Frame(frame21)
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
        frame24 = ttk.Frame(frame21)
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
        frame21.pack(side="top")
        notebook1.add(frame21, text='tab2')
        frame13 = ttk.Frame(notebook1)
        frame13.configure(height=200, width=200)
        canvas2 = tk.Canvas(frame13)
        canvas2.configure(width=240)
        canvas2.pack(anchor="n", expand=False, fill="y", side="left")
        frame14 = ttk.Frame(frame13)
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
        frame13.pack(side="top")
        notebook1.add(frame13, text='tab1')
        notebook1.pack(side="top")
        frame8 = ttk.Frame(mainWindow)
        frame8.configure(height=200, width=200)
        label6 = ttk.Label(frame8)
        label6.configure(
            state="disabled",
            text='TinyCore Forensics Edition 1.0 Installer')
        label6.pack(padx=5, side="left")
        separator4 = ttk.Separator(frame8)
        separator4.configure(orient="horizontal")
        separator4.pack(expand=True, fill="x", padx=5, side="top")
        frame8.pack(expand=True, fill="both", padx=10, pady=5, side="top")
        frame3 = ttk.Frame(mainWindow)
        frame3.configure(height=200, width=200)
        button1 = ttk.Button(frame3)
        button1.configure(text='Annulla')
        button1.pack(padx=10, side="right")
        button2 = ttk.Button(frame3)
        button2.configure(text='Avanti >')
        button2.pack(side="right")
        button3 = ttk.Button(frame3)
        button3.configure(text='< Indietro')
        button3.pack(side="right")
        frame3.pack(expand=True, fill="both", pady=10, side="top")

        # Main widget
        self.mainwindow = mainWindow

    def initTabs(self):
        pass

    def run(self):
        self.mainwindow.mainloop()

class WelcomePage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.configure(height=200, width=200)
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
        pass

class DiskFormatPage:
    def __init__(self) -> None:
        pass

class CustomDiskFormatPage:
    def __init__(self) -> None:
        pass

class InstallPage:
    def __init__(self) -> None:
        pass

class SetUsersPage:
    def __init__(self) -> None:
        pass

class FinishPage:
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    app = InstallerApp()
    app.run()
