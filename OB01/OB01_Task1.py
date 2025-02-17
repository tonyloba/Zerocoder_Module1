from datetime import datetime
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок: {self.due_date.strftime('%Y-%m-%d')}) - {status}"

class TaskManager():
    def __init__(self):
        self.tasks = []
    def add_task(self,description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_completed(self,description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return f"Задача '{description}' отмечена как выполненная."

        return f"Задача '{description}' не найдена."

    def delete_task(self,description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                return f"Задача '{description}' удалена."

        return f"Задача '{description}' не найдена."

    def show_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        if not pending_tasks:
            return ["Нет текущих задач."]
        return [str(task) for task in pending_tasks]

if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "2025-02-20")
    manager.add_task("Сделать отчет", "2025-02-18")
    print(manager.show_pending_tasks())
    print(manager.mark_task_completed("Сделать отчет"))
    print(manager.show_pending_tasks())