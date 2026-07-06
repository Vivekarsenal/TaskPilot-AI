# from pydantic import BaseModel
# from typing import List


# class ParsedInstruction(BaseModel):
#     goal: str
#     timeline: str
#     constraints: List[str]
#     # needs_clarification: bool
#     # questions: List[str]


# class TodoTask(BaseModel):
#     title: str
#     description: str
#     duration: str
#     priority: str


# class PlannerResponse(BaseModel):
#     tasks: List[TodoTask]

from pydantic import BaseModel
from typing import List


# class ParsedInstruction(BaseModel):
#     goal: str
#     timeline: str
#     constraints: List[str]
#     missing_information: List[str]

class ParsedInstruction(BaseModel):    # we have made chnages to add a human in a loop in the process
    goal: str
    timeline: str
    constraints: List[str]

    needs_clarification: bool
    questions: List[str]


class TodoTask(BaseModel):
    title: str
    description: str
    duration: str
    priority: str


class PlannerResponse(BaseModel):
    tasks: List[TodoTask]