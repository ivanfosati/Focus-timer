import tkinter as tk
from tkinter import ttk
import time

window = tk.Tk()
text_label = ttk.Label(window, text=time.strftime("%H" + ":" + "%M"), font=("Helvetica", 48))
text_label.pack(side="top")

window.mainloop()
