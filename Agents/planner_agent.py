import json

from Services.llm import LLMService
from Models.response import ParsedInstruction, PlannerResponse
from Prompts.planner_prompts import PLANNER_PROMPT


class PlannerAgent:

    def __init__(self, llm: LLMService):
        self.llm = llm

    def plan(self, parsed: ParsedInstruction) -> PlannerResponse:

        prompt = PLANNER_PROMPT.format(
            goal=parsed.goal,
            timeline=parsed.timeline,
            constraints=", ".join(parsed.constraints)
        )

        response = self.llm.generate(prompt)

        parsed_response = json.loads(response)

        return PlannerResponse(**parsed_response)