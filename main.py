from typing import List


class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, my_task) -> None:
        self.__tasks.append(my_task)

    @property
    def tasks(self) -> List[Task]:
        return self.__tasks


task_manager = TaskManager()

task_manager.add_task(Task("Задача 1", "Описание задачи 1"))
task_manager.add_task(Task("Задача 2", "Описание задачи 2"))
task_manager.add_task(Task("Задача 3", "Описание задачи 3"))

tasks = task_manager.tasks
for idx, task in enumerate(tasks, start=1):
    print(f"Задача {idx}: {task.title} - {task.description}")
