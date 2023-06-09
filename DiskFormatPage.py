import tkinter as tk
import tkinter.ttk as ttk
import parted

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.2f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.2f} Y{suffix}"

class DiskFormatPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        self.autoDiskFormat = tk.BooleanVar(value=True)
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
        radiobutton1 = ttk.Radiobutton(frame19, variable=self.autoDiskFormat, value=True)
        radiobutton1.configure(text='Automatico (usa intero disco)')
        radiobutton1.pack(anchor="w", padx=75, pady=5, side="top")
        radiobutton3 = ttk.Radiobutton(frame19, variable=self.autoDiskFormat, value=False)
        radiobutton3.configure(text='Manuale')
        radiobutton3.pack(anchor="w", padx=75, pady=5, side="top")
        frame19.pack(expand=True, fill="both", side="top")
        self.pack(side="top")

    def onButtonNextClick(self):
        if self.autoDiskFormat.get() == True:
            # TODO AutoFormat
            self.installerApp.navigateToPage("installPage")
        else:
            self.installerApp.navigateToPage("customDiskFormatPage")
    
    def onShow(self):
        self.installerApp.buttonBack["text"] = "< Indietro"
        self.installerApp.buttonBack["command"] = lambda : self.installerApp.navigateToPage("welcomePage")
        self.installerApp.buttonNext["command"] = lambda : self.onButtonNextClick()

class CustomDiskFormatPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
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
        frame25 = ttk.Frame(frame6)
        frame25.configure(height=200, width=200)
        label20 = ttk.Label(frame25)
        label20.configure(text='Disco di destinazione:')
        label20.pack(padx=(0, 5), side="left")
        self.combobox3 = ttk.Combobox(frame25, state="readonly")
        self.combobox3.pack(expand=True, fill="x", side="left")
        frame25.pack(fill="x", padx=50, pady=(0, 10), side="top")
        self.treeview1 = ttk.Treeview(frame6, columns=("C1", "C2", "C3", "C4"), show="headings", selectmode="browse")
        self.treeview1.column("#1")
        self.treeview1.heading("#1", text="Nome", anchor=tk.W)
        self.treeview1.column("#2")
        self.treeview1.heading("#2", text="Dimensione", anchor=tk.W)
        self.treeview1.column("#3")
        self.treeview1.heading("#3", text="Tipo", anchor=tk.W)
        self.treeview1.column("#4")
        self.treeview1.heading("#4", text="Filesystem", anchor=tk.W)
        self.treeview1.pack(expand=False, fill="x", padx=50, side="top")
        frame15 = ttk.Frame(frame6)
        frame15.configure(height=200, width=200)
        self.buttonNewPartition = ttk.Button(frame15)
        self.buttonNewPartition.configure(text='Nuova partizione...')
        self.buttonNewPartition.pack(side="left")
        self.buttonFormatPartition = ttk.Button(frame15)
        self.buttonFormatPartition.configure(text='Formatta...')
        self.buttonFormatPartition.pack(side="left")
        self.buttonDeletePartition = ttk.Button(frame15)
        self.buttonDeletePartition.configure(text='Elimina...')
        self.buttonDeletePartition.pack(side="left")
        frame15.pack(anchor="w", padx=50, pady=10, side="top")
        frame6.pack(expand=True, fill="both", side="top")
        self.pack(side="top")
    
    def loadDiskInfo(self):
        print(parted)
        self.devices = parted.getAllDevices()
        deviceList = list()
        for device in self.devices:
            deviceList.append(device.model + " - " + sizeof_fmt(device.length * device.sectorSize) + " (" + device.path + ")")
        self.combobox3["values"] = deviceList
        self.combobox3.current(0)

    def loadPartitions(self, device):
        for item in self.treeview1.get_children():
                self.treeview1.delete(item)
        try:
            disk = parted.newDisk(device)
            for primaryPartition in disk.getPrimaryPartitions():
                if primaryPartition.fileSystem.type == None:  
                    fileSystemName = "-"
                else:
                    fileSystemName = primaryPartition.fileSystem.type
                self.treeview1.insert(parent="", index='end', values=(primaryPartition.path, "Primaria", sizeof_fmt(primaryPartition.getSize(unit="b")), fileSystemName))
            extendedPartition = disk.getExtendedPartition()
            if extendedPartition:
                self.treeview1.insert(parent="", index='end', values=(primaryPartition.path, "Estesa", sizeof_fmt(primaryPartition.getSize(unit="b")), "-"))
        except:
            for item in self.treeview1.get_children():
                self.treeview1.delete(item)

    def onDiskComboBoxChange(self, event):
        self.loadPartitions(self.devices[self.combobox3.current()])
        self.buttonFormatPartition["state"] = "disabled"
        self.buttonDeletePartition["state"] = "disabled"

    def onDiskTreeViewSelect(self, event):
        if self.treeview1.selection():
            self.buttonFormatPartition["state"] = "enabled"
            self.buttonDeletePartition["state"] = "enabled"
        else:
            self.buttonFormatPartition["state"] = "disabled"
            self.buttonDeletePartition["state"] = "disabled"

    def onShow(self):
        self.installerApp.buttonBack["command"] = lambda : self.installerApp.navigateToPage("diskFormatPage")
        self.installerApp.buttonNext["command"] = lambda : self.installerApp.navigateToPage("installPage")
        self.loadDiskInfo()
        self.loadPartitions(self.devices[0])
        self.combobox3.bind('<<ComboboxSelected>>', self.onDiskComboBoxChange)
        self.treeview1.bind("<<TreeviewSelect>>", self.onDiskTreeViewSelect)

class NewPartitionDialog(ttk.Frame):
    def __init__(self, parent):
        pass