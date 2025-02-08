import tkinter as tk

# функция добавления задачи в список
def add_task():
    task = task_entry.get()
    if task:   # если задача есть, т.е. существует, то
        task_listbox.insert(tk.END, task) # добавляем ее в конец списка
        task_entry.delete(0, tk.END)  # очищаем поле ввода задачи c первого (0) до последнего (tk.END) символа

# функция удаления задачи из списка
def delete_task():
    selected_task = task_listbox.curselection() # функция для сохранения ID выбранного элемента
    if selected_task:
        task_listbox.delete(selected_task) # удаляем элемент по выбранному ID

# функция переноса выполненной задачи в список выполненных задач для контроля
def mark_task():
    selected_task = task_listbox.curselection()
    task = task_listbox.get(selected_task)
    task_redy_listbox.insert(tk.END, task)
    task_listbox.delete(selected_task)

# функция завершения контроля задачи и удаления ее из списка выполненных задач
def remove_task():
    selected_task = task_redy_listbox.curselection()
    if selected_task:
        task_redy_listbox.delete(selected_task)

# прописываем весь необходимый интерфейс
root = tk.Tk()
root.title('Task list') # название приложения
root.configure(bg='bisque') # цвет фона

text1 = tk.Label(root, text='Введите Вашу задачу', bg='burlywood3', fg='white') # вводим название окна ввода
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg='burlywood', fg='white') # окно ввода
task_entry.pack(pady=10) # закрепляем окно ввода на экране

add_task_button = tk.Button(root, text='Добавить задачу', bg='OliveDrab1', command=add_task) # добавляем клавишу ввода задачи
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text='Удалить задачу', bg='OrangeRed', command=delete_task) # добавляем клавишу удаления задачи
delete_button.pack(pady=5)

mark_button = tk.Button(root, text='Отметить выполненную задачу', bg='yellow', command=mark_task) # добавляем клавишу отметки и переноса выполненной задачи
mark_button.pack(pady=5)

remove_button = tk.Button(root, text='Завершить выполнение и контроль задачи', bg='OrangeRed', command=remove_task) # добавляем клавишу завершения выполнения и контроля задачи
remove_button.pack(pady=5)

text2 = tk.Label(root, text='Список задач', bg='LawnGreen', fg='white') # вводим название окна перечня задач
text2.pack(pady=5)

task_listbox = tk.Listbox(root, height=10, width=50, bg='OliveDrab1') # формируем окно перечня задач
task_listbox.pack(pady=10)

text3 = tk.Label(root, text='Список выполненных задач', bg='yellow', fg='black') # вводим название окна выполненных задач
text3.pack(pady=5)

task_redy_listbox = tk.Listbox(root, height=10, width=50, bg='yellow') # формируем окно выполненных задач
task_redy_listbox.pack(pady=10)

root.mainloop()
