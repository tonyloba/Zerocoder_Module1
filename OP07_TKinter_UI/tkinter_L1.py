import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("600x400")
# window.configure(bg="#f0f0f0")

def summa():
    num1 = entry.get().split()
    result = sum(map(int, num1))
    label2.config(text=f"Sum: {result}")



label2 = tk.Label(window, text="Enter numbers: ")
label2.pack()
entry = tk.Entry(window)

butn=tk.Button(window, text="Count!", command=summa)
butn.pack()

# entry.place(relx=10.5, rely=10.5, anchor="center")
entry.pack()

# label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 20))
label = tk.Label(window, text="Hello, Tkinter!!!!!!", font=("Arial", 20), fg="#0000ff", bg="#ffffff")
label.place(relx=0.5, rely=0.5, anchor="center")


def button_click():
    label.config(text="Button clicked!")

button1 = tk.Button(window, text="Click Me!", command=button_click, font=("Arial", 16), bg="#4CAF50", fg="#ffffff")
button2 = tk.Button(window, text="Click Me Again!", command=button_click, font=("Arial", 16), bg="#4CAF50", fg="#ffffff")
button1.place(relx=0.5, rely=0.6, anchor="center")
button2.place(relx=0.5, rely=0.7, anchor="center")
# button1.grid(row=10, column=0)
# button2.grid(row=11, column=1)
# button1.pack(pady=40)




window.mainloop()