import tkinter as tk
from tkinter import messagebox


def todo_list():
    root = tk.Tk()
    root.title("Трекер задач")
    root.geometry("700x400")
    root.configure(bg='#f0f0f5')
    return root
def add_to_new():
    task = task_entry.get()
    if task:
        new_tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    for listbox in [new_tasks_listbox, in_progress_listbox, closed_tasks_listbox]:
        for i in range(listbox.size()):
            if listbox.itemcget(i, "bg") == "lightblue":
                new_tasks_listbox.insert(tk.END, listbox.get(i))
                listbox.delete(i)


def delete_task():
    task = task_entry.get()
    if task:
        task_entry.delete(0, tk.END)
    # else:
    #     messagebox.showwarning("Удалить", "Пожалуйста, введите задачу.")
    deleted = False
    for listbox in [new_tasks_listbox, in_progress_listbox, closed_tasks_listbox]:
        for i in range(listbox.size()):
            if listbox.itemcget(i, "bg") == "lightblue":
                listbox.delete(i)
                deleted = True
    if deleted:
        messagebox.showinfo("Удалить", "Выбранные задачи были удалены.")
    elif not new_tasks_listbox.size() and not in_progress_listbox.size() and not closed_tasks_listbox.size():
        messagebox.showwarning("Удалить", "Нет задач для удаления.")
    else:
        messagebox.showwarning("Удалить", "Нет выбранных задач для удаления.")

def close_task():
    task = task_entry.get()
    if task:
        closed_tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    closed = False
    for listbox in [new_tasks_listbox, in_progress_listbox, closed_tasks_listbox]:
        for i in range(listbox.size()):
            if listbox.itemcget(i, "bg") == "lightblue":
                closed_tasks_listbox.insert(tk.END, listbox.get(i))
                listbox.delete(i)
                closed = True
    if closed:
        messagebox.showinfo("Закрыть", "Выбранные задачи были закрыты.")
    elif not new_tasks_listbox.size() and not in_progress_listbox.size() and not closed_tasks_listbox.size():
        messagebox.showwarning("Закрыть", "Нет задач для закрытия.")
    else:
        messagebox.showwarning("Закрыть", "Нет выбранных задач для закрытия.")

def move_to_work():
    task = task_entry.get()
    if task:
        in_progress_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    inWork=False
    for listbox in [new_tasks_listbox, in_progress_listbox, closed_tasks_listbox]:
        for i in range(listbox.size()):
            if listbox.itemcget(i, "bg") == "lightblue":
                in_progress_listbox.insert(tk.END, listbox.get(i))
                listbox.delete(i)
                inWork=True
    if inWork:
        messagebox.showinfo("В работу", "Выбранные задачи были перемещены в работу.")
    elif not new_tasks_listbox.size() and not in_progress_listbox.size() and not closed_tasks_listbox.size():
        messagebox.showwarning("В работу", "Нет задач для перемещения в работу.")
    else:
        messagebox.showwarning("В работу", "Нет выбранных задач для перемещения в работу.")

def mark_task():
    for listbox in [new_tasks_listbox, in_progress_listbox, closed_tasks_listbox]:
        selected_tasks = listbox.curselection()
        if selected_tasks:
            start = min(selected_tasks)
            end = max(selected_tasks)
            for i in range(start, end + 1):
                current_color = listbox.itemcget(i, "bg")
                new_color = "lightblue" if current_color != "lightblue" else "white"
                listbox.itemconfig(i, bg=new_color)
                listbox.selection_set(i)
                listbox.activate(i)
                listbox.see(i)
            return

# Добавляем обработчик события для кнопки Ctrl+Click
def on_click(event):
    if event.state & 0x0004:  # Ctrl+Click
        mark_task()

# Добавляем обработчик события для выделения мышью
def on_select(event):
    if event.state & 0x0004:  # Ctrl+Click
        mark_task()

root = tk.Tk()
root.title("Трекер задач")
root.geometry("700x400")
root.configure(bg='#f0f0f5')


# Colors
bg_color = '#e1e1e8'
button_color = '#4a4a72'
label_color = '#6a6a8c'
task_color = '#ffffff'

# Entry and Label for task input
task_label = tk.Label(root, text="Введите задачу:", bg=bg_color, fg=label_color)
task_label.pack(pady=(10, 0))
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=(0, 10))
#Adding Enter key
task_entry.bind("<Return>", lambda event: add_to_new())

# Buttons
buttons_frame = tk.Frame(root, bg=bg_color)
buttons_frame.pack(pady=10)

add_button = tk.Button(buttons_frame, text="Добавить в Новые задачи", bg=button_color, fg=task_color, command=add_to_new)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(buttons_frame, text="Удалить Задачу", bg=button_color, fg=task_color, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

mark_button = tk.Button(buttons_frame, text="Выбрать задачу", bg=button_color, fg=task_color, command=mark_task)
mark_button.grid(row=0, column=2, padx=5)

work_button = tk.Button(buttons_frame, text="Перевести в работу", bg=button_color, fg=task_color, command=move_to_work)
work_button.grid(row=0, column=3, padx=5)

close_button = tk.Button(buttons_frame, text="Закрыть задачу", bg=button_color, fg=task_color, command=close_task)
close_button.grid(row=0, column=4, padx=5)

# Task Columns
tasks_frame = tk.Frame(root, bg=bg_color)
tasks_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# New Tasks Column
new_tasks_label = tk.Label(tasks_frame, text="Новые задачи", bg=bg_color, fg=label_color)
new_tasks_label.grid(row=0, column=0, padx=10,sticky=tk.N+tk.S+tk.W+tk.E)

new_tasks_listbox = tk.Listbox(tasks_frame, bg=task_color, selectbackground="lightgrey", width=30, height=10)
new_tasks_listbox.grid(row=1, column=0, padx=10, pady=5,sticky=tk.N+tk.S+tk.W+tk.E)

# In Progress Column
in_progress_label = tk.Label(tasks_frame, text="Задачи в Работе", bg=bg_color, fg=label_color)
in_progress_label.grid(row=0, column=1, padx=10,sticky=tk.N+tk.S+tk.W+tk.E)

in_progress_listbox = tk.Listbox(tasks_frame, bg=task_color, selectbackground="lightgrey", width=30, height=10)
in_progress_listbox.grid(row=1, column=1, padx=10, pady=5,sticky=tk.N+tk.S+tk.W+tk.E)

# Closed Tasks Column
closed_tasks_label = tk.Label(tasks_frame, text="Закрытые задачи", bg=bg_color, fg=label_color)
closed_tasks_label.grid(row=0, column=2, padx=10,sticky=tk.N+tk.S+tk.W+tk.E)

closed_tasks_listbox = tk.Listbox(tasks_frame, bg=task_color, selectbackground="lightgrey", width=30, height=10)
closed_tasks_listbox.grid(row=1, column=2, padx=10, pady=5,sticky=tk.N+tk.S+tk.W+tk.E)

# Привязываем обработчики событий к спискам задач
for listbox in [new_tasks_listbox, in_progress_listbox, closed_tasks_listbox]:
    listbox.bind("<Control-1>", on_click)
    listbox.bind("<B1-Motion>", on_select)

# Set column weights to make them expandable
tasks_frame.columnconfigure(0, weight=1)
tasks_frame.columnconfigure(1, weight=1)
tasks_frame.columnconfigure(2, weight=1)

root.mainloop()

