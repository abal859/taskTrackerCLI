import json, utils

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    time = utils.cur_time()
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": time,
        "updatedAt": time,
    }
    tasks.append(task)
    save_tasks(tasks)

def del_task(id_task):
    id_task = int(id_task)
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != id_task]
    if len(new_tasks) < len(tasks):
        for i, task in enumerate(new_tasks, start=1):
            task["id"] = i
        save_tasks(new_tasks)

def update_task(id_task, new_description):
    time = utils.cur_time()
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id_task:
            task["description"] = new_description
            task["updatedAt"] = time
    save_tasks(tasks)

def mark_in_progress(id_task):
    time = utils.cur_time()
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id_task:
            task["status"] = "in-progress"
            task["updatedAt"] = time
    save_tasks(tasks)

def mark_done(id_task):
    time = utils.cur_time()
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id_task:
            task["status"] = "done"
            task["updatedAt"] = time
    save_tasks(tasks)

def list_all_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"{task}\n")

def list_done():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "done":
            print(f"{task}\n")

def list_todo():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "todo":
            print(f"{task}\n")
        
def list_in_progress():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "in-progress":
            print(task)
