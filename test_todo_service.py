from Services.todo_service import TodoService

todo = TodoService()

result = todo.generate(
    "Become a Java Backend Developer in 6 months"
)

print(result["parsed_instruction"])

print()

print(result["planner_response"])

print()

print(result["document"])