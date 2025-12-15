from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session

from app.students.router import get

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')

@router.get("/", summary="Получить всех студентов")
async def get_all_student(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.find_students(**request_body.to_dict())

@classmethod
async def find_students(cls, **student_data):
    async with async_session_maker() as session:
        # Запрос с фильтрацией по параметрам student_data
        query = select(cls.model).options(joinedload(cls.model.major)).filter_by(**student_data) 