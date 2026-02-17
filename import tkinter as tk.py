import tkinter as tk

root = tk.Tk()
root.title("Простой счетчик")
root.geometry("300x200")
counter = tk.IntVar(value=0)

def increase ():
    counter.set(counter.get() + 1)

def decrease ():
    counter.set(counter.get() - 1)
def reset():
    counter.set(0)
label = tk.Label(root, textvariable=counter, font=("Arial", 40))
label.pack(pady=20)
frame = tk.Frame(root)
frame.pack()
root.mainloop()
