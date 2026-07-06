# from fastapi import FastAPI
# from API.routes import router

# app = FastAPI(
#     title="LumiAI Todo Agent",
#     description="An AI-powered Todo List Generator using FastAPI and Gemini",
#     version="1.0.0"
# )

# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to LumiAI Todo Agent 🚀",
#         "docs": "http://127.0.0.1:8000/docs"
#     }

# app.include_router(router)


# from fastapi import FastAPI, HTTPException
# from Models.request import UserRequest
# from Services.todo_service import TodoService

# app = FastAPI()

# todo_service = TodoService()


# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to LumiAI Todo Agent 🚀",
#         "docs": "http://127.0.0.1:8000/docs"
#     }


# @app.post("/generate-todo")
# def generate_todo(request: UserRequest):

#     try:
#         return todo_service.generate(request.instruction)

#     except Exception as e:
#         import traceback

#         traceback.print_exc()      # Prints full error in terminal

#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )

from fastapi import FastAPI
from API.routes import router

app = FastAPI(
    title="TaskPilot AI",
    description="An AI-powered Multi-Agent Todo List Generator",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
    "message": "Welcome to TaskPilot AI 🚀",
    "docs": "http://127.0.0.1:8000/docs"
}


app.include_router(router)