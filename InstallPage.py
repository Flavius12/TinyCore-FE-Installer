from threading import Thread
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import stat
import shutil
from subprocess import Popen, PIPE
import time

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
        frame11 = tk.Frame(frame10, background="white")
        frame11.configure(height=200, width=200)
        bitmap = Image.open("res/header.png")
        bitmapTk = ImageTk.PhotoImage(bitmap)
        pictureBox4 = tk.Label(frame11, image=bitmapTk)
        pictureBox4.configure(width=112, height=48)
        pictureBox4.image = bitmapTk
        pictureBox4.pack(anchor="n", expand=False, fill="y", side="left")
        pictureBox4.pack(expand=False, fill="y", side="left")
        label7 = ttk.Label(frame11, background="white")
        label7.configure(font="{Arial} 12 {bold}", text='Installazione')
        label7.pack(anchor="w", padx=20, pady=(7, 0), side="top")
        label8 = ttk.Label(frame11, background="white")
        label8.configure(text='Installazione in corso...')
        label8.pack(anchor="w", padx=20, pady=(0, 5), side="top")
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
        print("DISK: " + params[0].device.path + " PART: " + params[1].path)
        destinationDev = os.path.basename(params[1].path)
        if params[2] != None:
            self.actions.append(Command("mkfs.{} {} -q -F".format(params[2], params[1].path), "Formattazione di {}".format(params[1].path)))
        self.actions.append(Mount(destinationDev, "Montaggio del disco di installazione"))
        self.actions.append(Copy(("/tmp/setup/vmlinuz", "/mnt/{}/boot/vmlinuz".format(destinationDev)))) # Must be the PURE TinyCore vmlinuz file, as extracted from the original ISO
        self.actions.append(Copy(("/tmp/setup/core.gz", "/mnt/{}/boot/core.gz".format(destinationDev)))) # Must be the PURE TinyCore core.gz file, as extracted from the original ISO
        # Copy extensions
        for file in self.recursiveListFiles("/tmp/builtin"):
            relPath = os.path.relpath(file, "/tmp/builtin")
            self.actions.append(Copy((file, "/mnt/{}/tce/{}".format(destinationDev, relPath))))
        # Change extensions permissions
        for file in self.recursiveListFiles("/mnt/{}/tce/optional".format(destinationDev)):
            self.actions.append(Chmod((file, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)))
        # Change extensions configuration files permissions 
        self.actions.append(Chmod(("/mnt/{}/tce/onboot.lst".format(destinationDev), stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)))    
        self.actions.append(Copy(("/opt/backgrounds/TCF.png", "/mnt/{}/opt/backgrounds/TCF.png".format(destinationDev))))
        self.actions.append(Copy(("/home/tc/.setbackground", "/mnt/{}/home/tc/.setbackground".format(destinationDev))))
        # Copy volatility3
        for file in self.recursiveListFiles("/home/tc/volatility3-master"):
            relPath = os.path.relpath(file, "/home/tc/volatility3-master")
            self.actions.append(Copy((file, "/mnt/{}/home/tc/volatility3-master/{}".format(destinationDev, relPath))))
        self.actions.append(Command("grub-install --boot-directory=/mnt/{}/boot {}".format(destinationDev, params[0].device.path), "Esecuzione di grub-install"))
        self.actions.append(Mkdir("/mnt/{}/boot/grub".format(destinationDev)))
        self.actions.append(Copy(("/opt/backgrounds/TCF.png", "/mnt/{}/boot/grub/TCF.png".format(destinationDev))))
        self.actions.append(Copy(("/tmp/setup/ascii.pf2", "/mnt/{}/boot/grub/fonts/ascii.pf2".format(destinationDev))))
        self.actions.append(GrubConfigure(("/mnt/{}".format(destinationDev), destinationDev)))
        self.actions.append(Unmount(destinationDev))
        #self.actions.append(Command("update-grub", "Esecuzione di update-grub"))
        self.progressBar["maximum"] = len(self.actions)
        self.installThread = InstallThread(self)
        self.installThread.start()
    
    def onFinishInstall(self):
        if self.fullStatus == False:
            messagebox.showerror("Installazione non completata correttamente", "Si sono verificati alcuni errori durante l'installazione del sistema. È consigliabile ripetere la procedura installazione nuovamente.")
        self.installerApp.navigateToPage("finishPage")

class InstallThread(Thread):
    def __init__(self, installPage):
        Thread.__init__(self)
        self.installPage = installPage
    
    def run(self):
        self.installPage.fullStatus = True
        for item in self.installPage.actions:
            self.installPage.labelProgress["text"] = item.description
            status = item.execute()
            print(item.description + " " + str(status))
            if self.installPage.fullStatus:
                self.installPage.fullStatus = status #Update fullStatus to False on any error
            self.installPage.progressBar["value"] += 1
        self.installPage.onFinishInstall()

class Action:
    def __init__(self, params, description=""):
        self._params = params
        self.description = description
    def execute(self):
        pass

class Command(Action):
    def execute(self):
        return os.system(self._params) == 0
    

class Mount(Action):
    def __init__(self, params, description=""):
        if description == "":
            super().__init__(params, "Montaggio della partizione /dev/{}".format(params))
        else:
            super().__init__(params, description)

    def execute(self):
        self.status = Mkdir("/mnt/{}".format(self._params)).execute()
        if self.status:
            return Command("mount /dev/{} /mnt/{}".format(self._params, self._params)).execute()
        return self.status

class Unmount(Action):
    def __init__(self, params, description=""):
        if description == "":
            super().__init__(params, "Smontaggio della partizione /dev/{}".format(params))
        else:
            super().__init__(params, description)

    def execute(self):
        self.status = Command("umount /dev/{}".format(self._params)).execute()
        if self.status:
            return Rmdir("/mnt/{}".format(self._params)).execute()
        return self.status
    
class Mkdir(Action):
    def __init__(self, params):
        super().__init__(params, "Creazione della cartella {}".format(params))
    def execute(self):
        try:
            if os.path.isdir(self._params) == False:
                os.mkdir(self._params)
            return True
        except:
            return False
    
class Rmdir(Action):
    def __init__(self, params):
        super().__init__(params, "Rimozione della cartella {}".format(params))
    def execute(self):
        try:
            if os.path.isdir(self._params) == True:
                shutil.rmtree(self._params)
            return True
        except:
            return False

class Copy(Action):
    def __init__(self, params):
        super().__init__(params, "Copia di {}".format(os.path.basename(params[0])))
    def execute(self):
        try:
            os.makedirs(os.path.dirname(self._params[1]), exist_ok=True)
            shutil.copy(self._params[0], self._params[1])
            return True
        except:
            return False

class Chmod(Action):
    def __init__(self, params):
        super().__init__(params, "Impostazione dei permessi su {}".format(os.path.basename(params[0])))
    def execute(self):
        try:
            os.chmod(self._params[0], self._params[1])
            return True
        except:
            return False

class GrubConfigure(Action):
    def __init__(self, params):
        super().__init__(params, "Configurazione del bootloader grub")
    def execute(self):
        try:
            deviceUUID = getDeviceUUID("/dev/{}".format(self._params[1]))
            grubConfigFile = open("{}/boot/grub/grub.cfg".format(self._params[0]), "w")
            grubConfigFile.write("set timeout=10\n")
            grubConfigFile.write("set timeout_style=menu\n")
            grubConfigFile.write("insmod ext3\n")
            grubConfigFile.write("insmod all_video\n")
            grubConfigFile.write("insmod efi_gop\n")
            grubConfigFile.write("insmod efi_uga\n")
            grubConfigFile.write("insmod ieee1275_fb\n")
            grubConfigFile.write("insmod vbe\n")
            grubConfigFile.write("insmod vga\n")
            grubConfigFile.write("insmod video_bochs\n")
            grubConfigFile.write("insmod video_cirrus\n")
            grubConfigFile.write("insmod gfxterm\n")
            grubConfigFile.write("insmod png\n")
            grubConfigFile.write("terminal_output gfxterm\n")
            grubConfigFile.write("search --no-floppy --fs-uuid --set=root {}\n".format(deviceUUID))
            grubConfigFile.write("loadfont /boot/grub/fonts/unicode.pf2\n")
            grubConfigFile.write("background_image /boot/grub/TCF.png\n")
            grubConfigFile.write("menuentry \"TinyCore Forensics Edition\"{\n")
            grubConfigFile.write("\tlinux /boot/vmlinuz quiet opt=UUID={} home=UUID={} tce=UUID={}\n".format(deviceUUID, deviceUUID, deviceUUID)) 
            grubConfigFile.write("\tinitrd /boot/core.gz\n")
            grubConfigFile.write("}")
            grubConfigFile.close()
            return True
        except:
            return False