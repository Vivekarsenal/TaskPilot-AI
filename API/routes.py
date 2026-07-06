from fastapi import APIRouter, HTTPException

from Models.request import UserRequest
from Services.todo_service import TodoService

router = APIRouter()

todo_service = TodoService()


@router.post("/generate-todo")
def generate_todo(request: UserRequest):
    try:
        result = todo_service.generate(request.instruction)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))