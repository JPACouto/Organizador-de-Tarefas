import json
import os

FILE_PATH = "data/tasks.json"


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(title):
    if not title.strip():
        raise ValueError("Título não pode ser vazio")

    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


def list_tasks():
    return load_tasks()


def complete_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise IndexError("Índice inválido")

    tasks[index]["done"] = True
    save_tasks(tasks)


def remove_task(index):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        raise IndexError("Índice inválido")

    tasks.pop(index)
    save_tasks(tasks)
