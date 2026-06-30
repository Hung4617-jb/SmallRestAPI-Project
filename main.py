from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = [
    {"id": 1, "title": "Einkaufen", "done": False},
    {"id": 2, "title": "8Kyu bearbeiten", "done": False}
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

class TodoCreate(BaseModel):
    title: str
    done: bool = False

@app.post("/todos")
def create_todo(todo: TodoCreate):
    new_id = max((t["id"] for t in todos), default=0) + 1
    new_todo = {"id": new_id, "title": todo.title, "done": todo.done}
    todos.append(new_todo)
    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted = todos.pop(index)
            return {"message": "Todo gelöscht", "todo": deleted}
    raise HTTPException(status_code=404, detail="Todo not found")