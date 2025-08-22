from database import engine, metadata_obj, get_connection
import models
from crud import create_task

from datetime import datetime

metadata_obj.create_all(engine)


title = input("title: ")
description = input("description: ")
due_date_text = input("due date (yyyy-mm-dd | hh:mm): ")

due_date = datetime.strptime(due_date_text, "%Y-%m-%d | %H:%M")

create_task(get_connection(), title, description=description, due_date=due_date)
