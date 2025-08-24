from datetime import datetime
from sqlalchemy import (
    Table, Column,
    Integer, String, DateTime, Boolean, Text
)
from database import metadata_obj

tasks = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(length=64), nullable=False),
    Column('description', Text, nullable=True),
    Column('completed', Boolean, nullable=False, default=False),
    Column('due_date', DateTime, default=datetime.utcnow),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime, default=datetime.utcnow)
)
##
