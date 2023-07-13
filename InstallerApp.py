import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from WelcomePage import WelcomePage
from DiskFormatPage import DiskFormatPage
from DiskFormatPage import CustomDiskFormatPage
from InstallPage import InstallPage
from FinishPage import FinishPage

class InstallerApp:
    def __init__(self):
        # build ui
        self.mainWindow = tk.Tk()
        self.quitRequestProcessed = False
        winWidth=500
        winHeight=360
        self.mainWindow.configure(width=winWidth, height=winHeight)
        self.mainWindow.eval("tk::PlaceWindow . center")
        self.mainWindow.title("TinyCore Forensic Edition 3.0 Installer")
        self.mainWindow.resizable(False, False)
        self.mainWindow.bind("<Destroy>", lambda args : self.onQuit())
        # Configure Styles
        style = ttk.Style()
        style.layout('Tabless.TNotebook.Tab', []) # turn off tabs
        style.configure('Tabless.TNotebook', borderwidth=0) # Flat style
        self.initTabs()
        frame8 = ttk.Frame(self.mainWindow)
        label6 = ttk.Label(frame8)
        label6.configure(
            state="disabled",
            text='TinyCore Forensic Edition 3.0 Installer')
        label6.pack(padx=5, side="left")
        separator4 = ttk.Separator(frame8)
        separator4.configure(orient="horizontal")
        separator4.pack(expand=True, fill="x", padx=5, side="top")
        frame8.pack(expand=True, fill="both", padx=10, pady=5, side="top")
        frame3 = ttk.Frame(self.mainWindow)
        self.buttonCancel = ttk.Button(frame3)
        self.buttonCancel.configure(text='Annulla', command=lambda : self.askQuit())
        self.buttonCancel.pack(padx=10, side="right")
        self.buttonNext = ttk.Button(frame3)
        self.buttonNext.configure(text='Avanti >')
        self.buttonNext.pack(side="right")
        self.buttonBack = ttk.Button(frame3)
        self.buttonBack.configure(text='< Indietro')
        self.buttonBack.pack(side="right")
        frame3.pack(expand=True, fill="both", pady=10, side="top")
        self.navigateToPage("welcomePage")

    def initTabs(self):
        self.notebook = ttk.Notebook(self.mainWindow, style="Tabless.TNotebook")
        self.notebook.configure(width=500, height=314)
        self.pages = {
            "welcomePage": WelcomePage(self, self.notebook),
            "diskFormatPage": DiskFormatPage(self, self.notebook),
            "customDiskFormatPage": CustomDiskFormatPage(self, self.notebook),
            "installPage": InstallPage(self, self.notebook),
            "finishPage": FinishPage(self, self.notebook),
        }
        for key, value in self.pages.items():
            self.notebook.add(value, text=key)
        self.notebook.pack(side="top")

    def navigateToPage(self, page, params=None):
        if page in self.pages:
            self.notebook.select(self.pages[page])
            self.pages[page].onShow(params)
            return True
        else:
            return False

    def run(self):
        self.mainWindow.mainloop()
    
    def quit(self):
        self.onQuit()
        self.mainWindow.quit()

    def askQuit(self):
        if messagebox.askquestion("Uscire dall'installazione?", "Vuoi uscire dall'installer di TinyCore Forensic Edition?", icon="warning") == "yes":
            self.quit()

    def onQuit(self):
        if not self.quitRequestProcessed:
            #os.system("reboot")
            self.quitRequestProcessed = True

if __name__ == "__main__":
    app = InstallerApp()
    app.run()
