from fastapi import FastAPI
from json import loads, dump
from os.path import getsize

app = FastAPI()


@app.get("/tasks")
def get_tasks():
    if getsize("data.json") > 0:
        with open("data.json", "r+") as json_file:

            task_data = loads(json_file.read())
            res = ""
            for task in task_data.values():
                res += f"Task {task[0]} status: {task[1]}."
            return res

    return f"No tasks yet."


@app.post("/tasks")
def create_task(task_id: str, task_name: str, status: str):

    with open("data.json", "r+") as json_file:
        if getsize("data.json") > 0:
            task_data = loads(json_file.read())
        else:
            task_data = {}
        if str(task_id) not in task_data:
            task_data[task_id] = [task_name, status]
            json_file.seek(0)
            json_file.truncate(0)
            dump(task_data, json_file, indent=4)
            return f"Task {task_data[task_id][0]} created."
        return f"Task with id {task_id} already exists."




@app.put("/tasks/{task_id}")
def update_task(task_id: str, new_status: str):
    if getsize("data.json") > 0:
        with open("data.json", "r+") as json_file:

                task_data = loads(json_file.read())
                if str(task_id) in task_data:
                    task_data[task_id] = [task_data[task_id][0], new_status]
                    json_file.seek(0)
                    json_file.truncate(0)
                    dump(task_data, json_file, indent=4)
                    return f"Task {task_data[task_id][0]} status has been changed to {new_status}"
                return "No such task."
    else:
        return "You haven't created any tasks yet."




@app.delete("/tasks/{task_id}")
def delete_task(task_id: str,):
    if getsize("data.json") > 0:
        with open("data.json", "r+") as json_file:

            task_data = loads(json_file.read())
            if str(task_id) in task_data:
                task_name = task_data.pop(str(task_id))[0]
                json_file.seek(0)
                json_file.truncate(0)
                dump(task_data, json_file, indent=4)

                return f"Task {task_name} has been deleted."
            return f"Task id {task_id} not found"
    else:
        return "You haven't created any tasks yet."
