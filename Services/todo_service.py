# import os
# import uuid

# from Agents.parser_agent import ParserAgent
# from Agents.planner_agent import PlannerAgent
# from Services.document_service import DocumentService
# from Services.llm import LLMService


# class TodoService:

#     def __init__(self):

#         self.llm = LLMService()

#         self.parser = ParserAgent(self.llm)

#         self.planner = PlannerAgent(self.llm)

#         self.document = DocumentService()

#     def generate(self, instruction: str):

#         # -------------------------
#         # Step 1 : Parse Instruction
#         # -------------------------

#         parsed_instruction = self.parser.parse(instruction)

#         # -------------------------
#         # Step 2 : Guardrail
#         # -------------------------

#         if parsed_instruction.missing_information:

#             return {
#                 "status": "needs_clarification",
#                 "questions": parsed_instruction.missing_information,
#                 "parsed_instruction": parsed_instruction.model_dump()
#             }

#         # -------------------------
#         # Step 3 : Planner
#         # -------------------------

#         planner_response = self.planner.plan(
#             parsed_instruction
#         )

#         # -------------------------
#         # Step 4 : Generate Document
#         # -------------------------

#         os.makedirs("output", exist_ok=True)

#         filename = f"output/todo_{uuid.uuid4().hex}.docx"

#         self.document.create_document(
#             planner_response,
#             filename
#         )

#         # -------------------------
#         # Step 5 : Success Response
#         # -------------------------

#         return {
#             "status": "success",
#             "parsed_instruction": parsed_instruction.model_dump(),
#             "planner_response": planner_response.model_dump(),
#             "document": filename
#         }

# def generate(self, instruction: str):

#     print("Step 1: Calling Parser...")

#     parsed_instruction = self.parser.parse(instruction)

#     print("Step 2: Parser Finished")

#     print(parsed_instruction)

#     if parsed_instruction.missing_information:
#         print("Step 3: Guardrail Triggered")

#         return {
#             "status": "needs_clarification",
#             "questions": parsed_instruction.missing_information,
#             "parsed_instruction": parsed_instruction.model_dump()
#         }

#     print("Step 4: Calling Planner")

#     planner_response = self.planner.plan(parsed_instruction)

#     print("Step 5: Planner Finished")


import os
import uuid

from Agents.parser_agent import ParserAgent
from Agents.planner_agent import PlannerAgent
from Services.document_service import DocumentService
from Services.llm import LLMService


class TodoService:

    def __init__(self):

        self.llm = LLMService()

        self.parser = ParserAgent(self.llm)

        self.planner = PlannerAgent(self.llm)

        self.document = DocumentService()

    def generate(self, instruction: str):

        parsed_instruction = self.parser.parse(
            instruction
        )
        if parsed_instruction.needs_clarification:
            return {
            "status": "needs_clarification",
            "message": "More information is required before generating a todo list.",
            "questions": parsed_instruction.questions
            }

        planner_response = self.planner.plan(
            parsed_instruction
        )

        os.makedirs("output", exist_ok=True)

        filename = f"output/todo_{uuid.uuid4().hex}.docx"

        self.document.create_document(
            planner_response,
            filename
        )

        return {
            "parsed_instruction": parsed_instruction.model_dump(),
            "planner_response": planner_response.model_dump(),
            "document": filename
        }
    # def generate(self, prompt: str) -> str:

    #  try:

    #     response = self.client.models.generate_content(
    #         model="gemini-2.5-flash",
    #         contents=prompt
    #     )

    #     return response.text

    #  except Exception as e:

    #     raise Exception(
    #         f"LLM Service Error: {str(e)}"
    #     )