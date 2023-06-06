import tkinter as tk
import tkinter.ttk as ttk

from WelcomePage import WelcomePage
from DiskFormatPage import DiskFormatPage
from DiskFormatPage import CustomDiskFormatPage
from InstallPage import InstallPage
from SetUsersPage import SetUsersPage
from FinishPage import FinishPage

class InstallerApp:
    def __init__(self):
        # build ui
        self.mainWindow = tk.Tk()
        self.mainWindow.configure(height=480, width=640)
        self.mainWindow.title("Installer")
        # Configure Styles
        style = ttk.Style()
        style.layout('Tabless.TNotebook.Tab', []) # turn off tabs
        style.configure('Tabless.TNotebook', borderwidth=0) # Flat style
        self.initTabs()
        frame8 = ttk.Frame(self.mainWindow)
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
        frame3 = ttk.Frame(self.mainWindow)
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

    def initTabs(self):
        self.notebook = ttk.Notebook(self.mainWindow, style="Tabless.TNotebook")
        self.notebook.configure(height=480, width=640)
        self.welcomePage = WelcomePage(self, self.notebook)
        self.notebook.add(self.welcomePage, text='Welcome Page')
        self.diskFormatPage = DiskFormatPage(self, self.notebook)
        self.notebook.add(self.diskFormatPage, text='Disk Format Page')
        self.customDiskFormatPage = CustomDiskFormatPage(self, self.notebook)
        self.notebook.add(self.customDiskFormatPage, text='Custom Disk Format Page')
        self.installPage = InstallPage(self, self.notebook)
        self.notebook.add(self.installPage, text='Install Page')
        self.setUsersPage = SetUsersPage(self, self.notebook)
        self.notebook.add(self.setUsersPage, text='Set Users Page')
        self.finishPage = FinishPage(self, self.notebook)
        self.notebook.add(self.finishPage, text='Finish Page')
        self.notebook.pack(side="top")

    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    app = InstallerApp()
    app.run()
