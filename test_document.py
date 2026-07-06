from Services.document_service import DocumentService
from Models.response import PlannerResponse, TodoTask

planner_response = PlannerResponse(
    tasks=[
        TodoTask(
            title="Learn Java Basics",
            description="Study variables, loops, methods and OOP.",
            duration="2 weeks",
            priority="High"
        ),
        TodoTask(
            title="Learn Spring Boot",
            description="Understand REST APIs and dependency injection.",
            duration="3 weeks",
            priority="High"
        )
    ]
)

document_service = DocumentService()

document_service.create_document(
    planner_response,
    "Output/generated_todo.docx"
)

print("Document generated successfully!")