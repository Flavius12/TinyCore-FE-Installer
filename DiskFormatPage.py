import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import parted

PRIMARY = 0
EXTENDED = 1
FREE = 2

#TODO Autoformat
#TODO New partitions
#TODO Format ext3 && rebuildfstab (does parted do this?)
#TODO Auto format if "Avanti >" on Unallocated Space

def getPartitions(disk):
    partitionList = list()
    for primaryPartition in disk.getPrimaryPartitions():
        partitionList.append((PRIMARY, primaryPartition))
    if disk.getExtendedPartition():
        partitionList.append((EXTENDED, disk.getExtendedPartition()))
    for freePartition in disk.getFreeSpacePartitions():
        if freePartition.geometry.end > 2048:
            partitionList.append((FREE, freePartition))
    partitionList.sort(key=lambda item: item[1].geometry.start)
    return partitionList

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
    
    def onShow(self, params):
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
            text='Seleziona la partizione su cui installare TinyCore Forensics Edition:')
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
        self.buttonNewPartition["state"] = "disabled"
        self.buttonNewPartition.pack(side="left")
        self.buttonDeletePartition = ttk.Button(frame15)
        self.buttonDeletePartition.configure(text='Elimina...')
        self.buttonDeletePartition["state"] = "disabled"
        self.buttonDeletePartition.pack(side="left")
        frame15.pack(anchor="w", padx=50, pady=10, side="top")
        frame6.pack(expand=True, fill="both", side="top")
        self.pack(side="top")
    
    def loadDiskInfo(self):
        print(parted)
        self.devices = parted.getAllDevices()
        self.disks = list()
        deviceList = list()
        for device in self.devices:
            #Load Disk
            try:
                self.disks.append(parted.newDisk(device))
            except:
                self.disks.append(parted.freshDisk(device, "msdos"))
            deviceList.append(device.model + " - " + sizeof_fmt(device.length * device.sectorSize) + " (" + device.path + ")")
        self.combobox3["values"] = deviceList
        self.combobox3.current(0)

    def loadPartitions(self, disk):
        for item in self.treeview1.get_children():
                self.treeview1.delete(item)
        try:
            self.partitionList = getPartitions(disk)
            for i, partition in enumerate(self.partitionList):
                if partition[0] == PRIMARY:
                    if partition[1].fileSystem.type == None:  
                        fileSystemName = "-"
                    else:
                        fileSystemName = partition[1].fileSystem.type
                    self.treeview1.insert(parent="", index='end', values=(partition[1].path, sizeof_fmt(partition[1].getSize(unit="b")), "Primaria", fileSystemName), tags=i)
                elif partition[0] == EXTENDED:
                    self.treeview1.insert(parent="", index='end', values=(partition[1].path, sizeof_fmt(partition[1].getSize(unit="b")), "Estesa", "-"), tags=i)
                else:
                    self.treeview1.insert(parent="", index="end", values=("Spazio non allocato", sizeof_fmt(partition[1].getSize(unit="b")), "-", "-"), tags=i)
        except:
            for item in self.treeview1.get_children():
                self.treeview1.delete(item)

    def onDiskComboBoxChange(self, event):
        self.loadPartitions(self.disks[self.combobox3.current()])
        self.buttonNewPartition["state"] = "disabled"
        self.buttonDeletePartition["state"] = "disabled"

    def onDiskTreeViewSelect(self, event):
        if self.treeview1.selection():
            selectedPartition = self.partitionList[self.treeview1.item(self.treeview1.focus())['tags'][0]]
            if selectedPartition[0] == PRIMARY or selectedPartition[0] == EXTENDED:
                self.buttonNewPartition["state"] = "disabled"
                self.buttonDeletePartition["state"] = "enabled"
            else:
                self.buttonNewPartition["state"] = "enabled"
                self.buttonDeletePartition["state"] = "disabled"
        else:
            self.buttonNewPartition["state"] = "disabled"
            self.buttonDeletePartition["state"] = "disabled"
        
    def onButtonNewPartitionClick(self):
        resp = NewPartitionDialog(self.installerApp.mainWindow, self.partitionList[self.treeview1.item(self.treeview1.focus())['tags'][0]][1]).response
        print("RESPONSE " + str(resp))

    def onButtonDeletePartitionClick(self):
        if messagebox.askquestion("Cancellare la partizione?", "Vuoi cancellare la partizione selezionata?\nATTENZIONE: TUTTI I DATI IN QUESTA PARTIZIONE SARANNO CANCELLATI", icon="warning") == "yes":
            self.disks[self.combobox3.current()].deletePartition(self.partitionList[self.treeview1.item(self.treeview1.focus())['tags'][0]][1])
            self.loadPartitions(self.disks[self.combobox3.current()]) #Update partitions TreeView

    def onButtonNextClick(self):
        if self.treeview1.selection():
            selectedPartition = self.partitionList[self.treeview1.item(self.treeview1.focus())['tags'][0]]
            if selectedPartition[0] == PRIMARY or selectedPartition[0] == FREE:
                if selectedPartition[0] == FREE: #Format the partition now
                    pass #TODO Program later
                else:
                    if messagebox.askquestion("Scrivere le modifiche sul disco?", "Proseguendo, si procederà con il partizionamento del disco {} e l'installazione del sistema sulla partizione {}. Continuare?\nATTENZIONE: TUTTI I DATI PRESENTI SUL DISCO SARANNO CANCELLATI".format(self.disks[self.combobox3.current()].device.path, selectedPartition[1].path), icon="warning") == "yes":
                        self.disks[self.combobox3.current()].commit()
                        self.installerApp.navigateToPage("installPage", (self.disks[self.combobox3.current()].device.path, selectedPartition[1].path))
            else:
                messagebox.showerror("Partizione non valida", "Il sistema può essere installato solo su partizioni primarie")
        else:
            messagebox.showerror("Nessuna partizione selezionata", "Selezionare la partizione in cui si desidera installare il sistema")

    def onShow(self, params):
        self.installerApp.buttonBack["command"] = lambda : self.installerApp.navigateToPage("diskFormatPage")
        self.installerApp.buttonNext["command"] = lambda : self.onButtonNextClick()
        self.buttonNewPartition["command"] = lambda : self.onButtonNewPartitionClick()
        self.buttonDeletePartition["command"] = lambda : self.onButtonDeletePartitionClick()
        self.loadDiskInfo()
        self.loadPartitions(self.disks[0])
        self.combobox3.bind('<<ComboboxSelected>>', self.onDiskComboBoxChange)
        self.treeview1.bind("<<TreeviewSelect>>", self.onDiskTreeViewSelect)

class NewPartitionDialog(tk.Toplevel):
    def __init__(self, parent, partition):
        super().__init__(parent)
        self.response = False
        self.startSector = partition.geometry.start
        self.primaryPartition = tk.BooleanVar(value=True)
        self.partitionSize = tk.StringVar(value=partition.getSize(unit="MB"))
        self.posX = parent.winfo_x() + (parent.winfo_width() / 2 - 345 / 2)
        self.posY = parent.winfo_y() + (parent.winfo_height() / 2 - 130 / 2)
        self.geometry("345x130+{}+{}".format(int(self.posX), int(self.posY)))
        #self.positionfrom(who="program")
        self.attributes('-topmost', True)
        self.title("Nuova partizione...")
        label15 = ttk.Label(self)
        label15.configure(relief="flat", takefocus=False, text='Tipo:')
        label15.grid(column=0, padx=10, row=0, sticky="e")
        frame26 = ttk.Frame(self)
        radiobutton5 = ttk.Radiobutton(frame26, variable=self.primaryPartition, value=True)
        radiobutton5.configure(text='Primaria')
        radiobutton5.pack(side="left")
        radiobutton6 = ttk.Radiobutton(frame26, variable=self.primaryPartition, value=False)
        radiobutton6.configure(text='Estesa')
        radiobutton6.pack(padx=20, side="left")
        frame26.grid(column=1, row=0, sticky="w")
        self.label18 = ttk.Label(self)
        self.label18.configure(text='Filesystem:')
        self.label18.grid(column=0, padx=10, row=1, sticky="e")
        self.combobox1 = ttk.Combobox(self)
        self.combobox1.configure(validate="none")
        self.combobox1["values"] = ["ext3"]
        self.combobox1.current(0)
        self.combobox1.grid(column=1, row=1, sticky="w")
        label29 = ttk.Label(self)
        label29.configure(text='Dimensione:')
        label29.grid(column=0, padx=10, row=2, sticky="e")
        frame20 = ttk.Frame(self)
        spinbox2 = ttk.Spinbox(frame20, from_=0.5, to=partition.getSize(unit="MB"), textvariable=self.partitionSize)
        spinbox2.pack(side="left")
        label31 = ttk.Label(frame20)
        label31.configure(text='MB')
        label31.pack(padx=5, side="left")
        frame20.grid(column=1, row=2, sticky="w")
        frame27 = ttk.Frame(self)
        self.button5 = ttk.Button(frame27)
        self.button5.configure(text='Annulla')
        self.button5.pack(side="left")
        self.button4 = ttk.Button(frame27)
        self.button4.configure(text='OK')
        self.button4.pack(padx=5, side="left")
        frame27.grid(column=1, row=3, sticky="e")
        self.rowconfigure("all", pad=10)
        self.columnconfigure("all", pad=10)
        radiobutton5["command"] = lambda : self.onRadioButtonPrimarySelected()
        radiobutton6["command"] = lambda : self.onRadioButtonExtendedSelected()
        self.button5["command"] = lambda : self.onButtonCancelClick()
        self.button4["command"] = lambda : self.onButtonOkClick()
        self.grab_set()
        self.wait_window()

    def onRadioButtonPrimarySelected(self):
        self.label18["state"] = "enabled"
        self.combobox1["state"] = "enabled"

    def onRadioButtonExtendedSelected(self):
        self.label18["state"] = "disabled"
        self.combobox1["state"] = "disabled"

    def onButtonCancelClick(self):
        self.response = False
        self.destroy()

    def onButtonOkClick(self):
        self.response = True
        self.destroy()