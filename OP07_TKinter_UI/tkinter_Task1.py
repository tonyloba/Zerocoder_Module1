import tkinter as tk

def get_name():
    label2.config(text=f"Hello, {entry.get()}")

window = tk.Tk()
window.title("My First GUI")
window.geometry("600x400")

label = tk.Label(window, text="Enter your name: ")
label.pack()
entry = tk.Entry(window)
entry.pack()

butn=tk.Button(window, text="Save", command=get_name)
butn.pack()

label2 = tk.Label(window, text=f"Hello")
label2.pack()

window.mainloop()