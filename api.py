from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Todos API — ПЗ №6",
    description="Использование шаблонов Jinja2 в FastAPI (студент Митрофанов Лев)",
    version="1.0.0"
)

@app.get("/")
async def welcome() -> dict:
    return {"message": "Митрофанов Лев — Шаблоны в FastAPI (ПЗ №6)"}

app.include_router(todo_router)
