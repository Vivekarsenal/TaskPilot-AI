from Services.llm import LLMService
from Agents.planner_agent import PlannerAgent
from Models.response import ParsedInstruction

llm = LLMService()

planner = PlannerAgent(llm)

instruction = ParsedInstruction(
    goal="Become a Java Backend Developer",
    timeline="6 months",
    constraints=[],
    missing_information=[]
)

result = planner.plan(instruction)

print(result)