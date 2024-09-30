from typing import Union

import json
from ToDo import TaskManager
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

class Task(BaseModel):
    description: str
    completed: bool
    due_date: str
    category: str
    reminder: bool

tasks = TaskManager()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    with open("tasks.json","r") as file:
        data=json.load(file)
    return {"tasks": data}

@app.get("/{id}")
def getTask(id:int):
    with open("tasks.json","r") as file:
        data=json.load(file)
    return {"task": data[id]}

@app.post('/')
async def createTask(task: Task):
    taskCreate = task.dict()
    tasks.add_task(taskCreate["description"], taskCreate["due_date"],  taskCreate["category"])
    return {"message":"se agrego correctamente"}


@app.delete('/{id}')
async def deleteTask(id:int):
    print(id)
    tasks.delete_task(id)
    return {"message":"se elimino correctamente"}


@app.put('/{id}')
async def editTask(id:int,task:Task):
    taskEdit = task.dict()
    tasks.edit_task(id,taskEdit["description"])
    return {"message":"se edito correctamente"}

