from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключаем маршруты
app.include_router(user.router)
app.include_router(task.router)
