import tkinter as tk

root = tk.Tk()
root.title("Простой счетчик")
root.geometry("300x200")
counter = tk.IntVar(value=0)

def increase ():
    counter.set(counter.get() + 1)

def decrease ():
    counter.set(counter.get() - 1)

root.mainloop()
