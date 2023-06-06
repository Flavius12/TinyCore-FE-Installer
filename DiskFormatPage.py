import tkinter as tk
import tkinter.ttk as ttk

class DiskFormatPage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        frame17 = ttk.Frame(self)
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
        frame19 = ttk.Frame(self)
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
        self.pack(side="top")

class CustomDiskFormatPage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        frame5 = ttk.Frame(self)
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
        frame6 = ttk.Frame(self)
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
        self.pack(side="top")