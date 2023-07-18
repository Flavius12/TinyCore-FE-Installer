import sys
import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    if len(sys.argv) == 2 and sys.argv[1] == '0':
        messagebox.showinfo("Installazione completata", "L'installazione è stata completata, il sistema verrà riavviato. Rimuovere eventuali dischi dalle unità ottiche.")
    else: 
        messagebox.showwarning("Installazione annullata", "L'installazione è stata annullata, il sistema verrà riavviato.")
