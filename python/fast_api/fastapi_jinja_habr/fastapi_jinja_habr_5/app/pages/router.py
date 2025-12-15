from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.students.router import get

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')

@router.get("/", summary="Получить всех студентов")
async def get_all_student(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.find_students(**request_body.to_dict())

# @router.get('/students')
# async def get_student_html(request: Request):
#     return templates.TemplateResponse(name='students.html', context={'request': request})

@router.get('/students')
async def get_students_html(request: Request, user=Depends(get_all_st)) -> list[SStudent]:
    return templates.TemplateResponse(name='student.html', context={'request': request})