from threading import Thread
import tkinter as tk
import tkinter.ttk as ttk
import os
import stat
import shutil
from subprocess import Popen, PIPE
import time

#TODO Copy necessary files (only forensics tools part missing)
#TODO Desktop wallpaper install
#TODO GRUB wallpaper install

def getDeviceUUID(device):
    response = Popen(["blkid", "-s", "UUID", "-o", "value", device], stdout=PIPE).communicate()
    return response[0].decode("utf-8").replace("\n", "")

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

    def recursiveListFiles(self, path):
        fileList = []
        for root, dirs, files in os.walk(path):
            for file in files:
                fileList.append(os.path.normpath(os.path.join(root, file)))
        return fileList

    def onShow(self, params):
        self.installerApp.buttonBack["state"] = "disabled"
        self.installerApp.buttonNext["state"] = "disabled"
        self.installerApp.buttonCancel["state"] = "disabled"
        print("DISK: " + params[0] + " PART: " + params[1])
        sourceDisk = "/media/flavius12/" # TODO Get install disk automatically
        installPartitionBasename = os.path.basename(params[1])
        if params[2] != None:
            self.actions.append(Command("mkfs.{} {}".format(params[2], params[1]), "Formattazione di {}".format(params[1])))
        self.actions.append(Mount(installPartitionBasename))
        self.actions.append(Mount(installPartitionBasename, "Montaggio del disco di installazione")) #TODO DISK instead of installPartitionBasename
        self.actions.append(Copy(("/home/flavius12/Desktop/gui.py", "/mnt/{}/gui.py".format(installPartitionBasename))))
        self.actions.append(Copy(("{}/TinyCore/boot/vmlinuz".format(sourceDisk), "/mnt/{}/boot/vmlinuz".format(installPartitionBasename))))
        self.actions.append(Copy(("{}/TinyCore/boot/core.gz".format(sourceDisk), "/mnt/{}/boot/core.gz".format(installPartitionBasename))))
        # Copy extensions
        for file in self.recursiveListFiles("{}/TinyCore/cde".format(sourceDisk)):
            relPath = os.path.relpath(file, "{}/TinyCore/cde".format(sourceDisk))
            self.actions.append(Copy((file, "/mnt/{}/tce/{}".format(installPartitionBasename, relPath))))
        # Change extensions permissions
        for file in self.recursiveListFiles("/mnt/{}/tce/optional".format(installPartitionBasename)):
            self.actions.append(Chmod((file, stat.S_IRUSR or stat.S_IWUSR or stat.S_IRGRP or stat.S_IWGRP or stat.S_IROTH)))
        # Change extensions configuration files permissions
        self.actions.append(Chmod(("/mnt/{}/tce/copy2fs.lst".format(installPartitionBasename), stat.S_IRUSR or stat.S_IWUSR or stat.S_IRGRP or stat.S_IWGRP or stat.S_IROTH)))    
        self.actions.append(Chmod(("/mnt/{}/tce/onboot.lst".format(installPartitionBasename), stat.S_IRUSR or stat.S_IWUSR or stat.S_IRGRP or stat.S_IWGRP or stat.S_IROTH)))    
        self.actions.append(Chmod(("/mnt/{}/tce/xbase.lst".format(installPartitionBasename), stat.S_IRWXU or stat.S_IRWXG or stat.S_IRWXO)))    
        self.actions.append(Command("grub-install --boot-directory=/mnt/{}/boot {}".format(installPartitionBasename, params[0]), "Esecuzione di grub-install"))
        self.actions.append(Mkdir("/mnt/{}/boot/grub".format(installPartitionBasename)))
        self.actions.append(GrubConfigure(("/mnt/{}".format(installPartitionBasename), installPartitionBasename)))
        #self.actions.append(Command("update-grub", "Esecuzione di update-grub"))
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
            #time.sleep(1) #TODO REMOVE LATER
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
        os.makedirs(os.path.dirname(self._params[1]), exist_ok=True)
        shutil.copy(self._params[0], self._params[1])

class Chmod(Action):
    def __init__(self, params):
        super().__init__(params, "Impostazione dei permessi su {}".format(os.path.basename(params[0])))
    def execute(self):
        os.chmod(self._params[0], self._params[1])

class GrubConfigure(Action):
    def __init__(self, params):
        super().__init__(params, "Configurazione del bootloader grub")
    def execute(self):
        deviceUUID = getDeviceUUID("/dev/{}".format(self._params[1]))
        grubConfigFile = open("{}/boot/grub/grub.cfg".format(self._params[0]), "w")
        grubConfigFile.write("insmod ext3\n")
        grubConfigFile.write("search --no-floppy --fs-uuid --set=root {}".format(deviceUUID))
        grubConfigFile.write("menuentry \"TinyCore Forensics Edition\"{\n")
        grubConfigFile.write("\troot=(hd1,msdos3)\n") #TODO Parametrize hd1 and msdos3!!!
        grubConfigFile.write("\tlinux /boot/vmlinuz quiet opt=UUID={} home=UUID={} tce=UUID={}\n".format(deviceUUID, deviceUUID, deviceUUID)) 
        grubConfigFile.write("\tinitrd /boot/core.gz\n")
        grubConfigFile.write("}")
        grubConfigFile.close()