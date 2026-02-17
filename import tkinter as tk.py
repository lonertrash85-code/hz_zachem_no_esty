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
btn_increase = tk.Button(frame, text="+", width=5, command=increase)
btn_increase.grid(row=0, column=0, padx=5)

btn_decrease = tk.Button(frame, text="-", width=5, command=decrease)
btn_decrease.grid(row=0, column=1, padx=5)

btn_reset = tk.Button(root, text="Сброс", command=reset)
btn_reset.pack(pady=10)
root.mainloop()
