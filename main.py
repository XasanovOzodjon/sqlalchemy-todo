from database import engine, metadata_obj, get_connection
import models
from crud import create_task, get_tasks, delete_task, update_task

from datetime import datetime

metadata_obj.create_all(engine)


def add_tasks():
    title = input("title: ")
    description = input("description: ")
    due_date_text = input("due date (yyyy-mm-dd | hh:mm): ")

    due_date = datetime.strptime(due_date_text, "%Y-%m-%d | %H:%M")

    create_task(get_connection(), title, description=description, due_date=due_date)


def show_tasks():
    result = get_tasks(get_connection())

    for row in result:
        print(row)

def remove_task():
    task_id = int(input("task id: "))
    delete_task(get_connection(), task_id)

def edit_task():
    task_id = int(input("task id: "))

    update_task(get_connection(), task_id, title="Edited Task")

show_tasks()
edit_task()


