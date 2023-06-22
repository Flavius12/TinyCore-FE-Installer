from threading import Thread
import tkinter as tk
import tkinter.ttk as ttk
import os
import shutil
import time

#TODO Copy necessary files
#TODO Install GRUB
#TODO Test GRUB menu.lst file

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
        installPartitionBasename = os.path.basename(params[1])
        if params[2] != None:
            self.actions.append(Command("mkfs.{} {}".format(params[2], params[1]), "Formattazione di {}".format(params[1])))
        self.actions.append(Mount(installPartitionBasename))
        self.actions.append(Mount(installPartitionBasename, "Montaggio del disco di installazione")) #TODO DISK instead of installPartitionBasename
        self.actions.append(Copy(("/home/flavius12/Desktop/gui.py", "/mnt/{}/gui.py".format(installPartitionBasename))))
        self.actions.append(GrubConfigure("/mnt/" + installPartitionBasename))               
        self.progressBar["maximum"] = len(self.actions)
        self.installThread = InstallThread(self)
        self.installThread.start()
    
    def onFinishInstall(self):
        self.installerApp.navigateToPage("setUsersPage")

class InstallThread(Thread):
    def __init__(self, installPage):
        Thread.__init__(self)
        self.installPage = installPage
    
    def run(self):
        for item in self.installPage.actions:
            self.installPage.labelProgress["text"] = item.description
            item.execute()
            self.installPage.progressBar["value"] += 1
            time.sleep(1)
        self.installPage.onFinishInstall()

class Action:
    def __init__(self, params, description=""):
        self._params = params
        self.description = description
    def execute(self):
        pass

class Command(Action):
    def execute(self):
        return os.system(self._params)
    

class Mount(Action):
    def __init__(self, params, description=""):
        if description == "":
            super().__init__(params, "Montaggio della partizione /dev/{}".format(params))
        else:
            super().__init__(params, description)

    def execute(self):
        Mkdir("/mnt/{}".format(self._params)).execute()
        Command("mount /dev/{} /mnt/{}".format(self._params, self._params)).execute()

class Unmount(Action):
    def __init__(self, params, description=""):
        if description == "":
            super().__init__(params, "Smontaggio della partizione /dev/{}".format(params))
        else:
            super().__init__(params, description)

    def execute(self):
        Command("umount /mnt/{}".format(self._params)).execute()
        Rmdir("/mnt/{}".format(self._params)).execute()
    
class Mkdir(Action):
    def __init__(self, params):
        super().__init__(params, "Creazione della cartella {}".format(params))
    def execute(self):
        if os.path.isdir(self._params) == False:
            os.mkdir(self._params)
    
class Rmdir(Action):
    def __init__(self, params):
        super().__init__(params, "Rimozione della cartella {}".format(params))
    def execute(self):
        if os.path.isdir(self._params) == True:
            os.rmdir(self._params)

class Copy(Action):
    def __init__(self, params):
        super().__init__(params, "Copia di {}".format(os.path.basename(params[0])))
    def execute(self):
        shutil.copy(self._params[0], self._params[1])

class GrubConfigure(Action):
    def __init__(self, params):
        super().__init__(params, "Configurazione del bootloader grub")
    def execute(self):
        grubConfigFile = open("{}/menu.lst".format(self._params), "w")
        grubConfigFile.write("default 0\n")
        grubConfigFile.write("timeout 10\n")
        grubConfigFile.write("title tinycore\n") #TODO Proper title
        grubConfigFile.write("kernel /boot/bzImage quiet\n")
        grubConfigFile.write("initrd /boot/tinycore.gz\n")
        grubConfigFile.close()