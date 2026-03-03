import tkinter as tk
from ui.main_window import ElectoralDataManager

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1200x700')
    app = ElectoralDataManager(root)
    root.mainloop()