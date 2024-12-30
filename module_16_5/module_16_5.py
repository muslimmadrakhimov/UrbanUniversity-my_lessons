from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

# Инициализация приложения FastAPI
app = FastAPI()

# Подключаем папку для шаблонов
templates = Jinja2Templates(directory="templates")

# Статические файлы, если нужно
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Список пользователей, где мы будем хранить данные
users = []

# Определяем модель пользователя
class User(BaseModel):
    id: int  # Идентификатор пользователя
    username: str  # Имя пользователя
    age: int  # Возраст пользователя

# 1. Главная страница со списком пользователей
@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse(
        "users.html",
        {"request": request, "users": users}  # Передаем request и список пользователей
    )

# 2. POST запрос для добавления нового пользователя
@app.post("/user/", response_model=User)
async def post_user(user: User):
    # Если список пользователей пустой, присваиваем id = 1
    user_id = users[-1].id + 1 if users else 1

    # Создаем нового пользователя
    new_user = User(id=user_id, username=user.username, age=user.age)

    # Добавляем пользователя в список
    users.append(new_user)

    # Возвращаем созданного пользователя
    return new_user

# 3. GET запрос для просмотра информации о конкретном пользователе
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(request: Request, user_id: int):
    # Ищем пользователя по id
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")

    return templates.TemplateResponse(
        "users.html",
        {"request": request, "user": user}  # Передаем request и объект пользователя
    )

# 4. PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    # Ищем пользователя по id
    for existing_user in users:
        if existing_user.id == user_id:
            # Если нашли пользователя, обновляем его данные
            existing_user.username = user.username
            existing_user.age = user.age
            return existing_user

    # Если пользователя с таким id нет, выбрасываем ошибку
    raise HTTPException(status_code=404, detail="User was not found")

# 5. DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    # Ищем пользователя по id
    for user in users:
        if user.id == user_id:
            # Если нашли пользователя, удаляем его из списка
            users.remove(user)
            return user

    # Если пользователя с таким id нет, выбрасываем ошибку
    raise HTTPException(status_code=404, detail="User was not found")
