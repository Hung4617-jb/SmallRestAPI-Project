from fastapi import FastAPI, HTTPException

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