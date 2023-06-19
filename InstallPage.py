from threading import Thread
import tkinter as tk
import tkinter.ttk as ttk
import os
import time

class InstallPage(ttk.Frame):
    def __init__(self, installerApp, parent):
        ttk.Frame.__init__(self)
        self.installerApp = installerApp
        self.actions = []
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
        self.labelProgress = ttk.Label(frame12)
        self.labelProgress.configure(text='Inizializzazione dell\'installer...')
        self.labelProgress.pack(expand=False, fill="x", padx=50, pady=10, side="top")
        self.progressBar = ttk.Progressbar(frame12)
        self.progressBar.configure(orient="horizontal", value=0)
        self.progressBar.pack(fill="x", padx=50, side="top")
        frame12.pack(expand=True, fill="both", side="top")
        self.pack(side="top")

    def onShow(self, params):
        self.installerApp.buttonBack["state"] = "disabled"
        self.installerApp.buttonNext["state"] = "disabled"
        self.installerApp.buttonCancel["state"] = "disabled"
        print("DISK: " + params[0] + " PART: " + params[1])
        if params[2] != None:
            self.actions.append(Command("mkfs.{} {}".format(params[2], params[1]), "Formattazione di {}".format(params[1])))
        self.actions.append(Command("mount {}".format(params[1]), "Montaggio della partizione {}".format(params[1])))
        self.actions.append(Command("mount /dev/hdc", "Montaggio del disco di installazione"))
        self.actions.append(Copy(("/home/flavius12/Desktop/gui.py", "{}/gui.py".format(params[1]))))                 
        #self.installerApp.navigateToPage("setUsersPage")
        self.progressBar["maximum"] = 3
        self.installThread = InstallThread(self.labelProgress, self.progressBar, self.actions)
        self.installThread.start()

class InstallThread(Thread):
    def __init__(self, labelProgress, progressBar, actions):
        Thread.__init__(self)
        self.labelProgress = labelProgress
        self.progressBar = progressBar
        self.actions = actions
    
    def run(self):
        for item in self.actions:
            self.labelProgress["text"] = item.description
            print(item.description)
            item.execute()
            print("sTEP")
            self.progressBar["value"] += 1
            time.sleep(1)
            

class Action:
    def __init__(self, params, description):
        self._params = params
        self.description = description
    def execute(self):
        pass

class Command(Action):
    def execute(self):
        return os.system(self._params)
    
class MkDir(Action):
    def __init__(self, params):
        super().__init__(self, params, "Creazione della cartella {}".format(params))
    def execute(self):
        pass #TODO MkDir Command
    
class Copy(Action):
    def __init__(self, params):
        super().__init__(params, "Copia di {}".format(os.path.basename(params[0])))
    def execute(self):
        pass #TODO Copy Command

class GrubConfigure(Action):
    def __init__(self, params):
        super().__init__(self, params, "Configurazione del bootloader grub")
    def execute(self):
        pass #TODO Create menu.lst file 
        # default 0
        # timeout 10
        # title tinycore
        # kernel /boot/bzImage quiet
        # initrd /boot/tinycore.gz