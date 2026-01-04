# todo.py

tasks = []


def add_task(name):
    """Add a new task to the to-do list."""
    if not name or name.strip() == "":
        raise ValueError("Task name cannot be empty")

    task = {
        "id": len(tasks) + 1,
        "name": name,
        "completed": False
    }
    tasks.append(task)
    return task


def delete_task(task_id):
    """Delete a task by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return task
    raise ValueError("Task not found")


def edit_task(task_id, new_name):
    """Edit the name of an existing task."""
    if not new_name or new_name.strip() == "":
        raise ValueError("New task name cannot be empty")

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            return task
    raise ValueError("Task not found")
