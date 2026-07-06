from Models.request import UserRequest
from Models.response import ParsedInstruction, TodoTask, PlannerResponse

request = UserRequest(
    instruction="Become a Java Backend Developer in 6 months"
)

parsed = ParsedInstruction(
    goal="Become Java Backend Developer",
    timeline="6 months",
    constraints=[],
    missing_information=[]
)

task = TodoTask(
    title="Learn Java",
    description="Study Java fundamentals",
    duration="2 weeks",
    priority="High"
)

plan = PlannerResponse(tasks=[task])

print(request)
print(parsed)
print(plan)