# import json

# from Services.llm import LLMService
# from Prompts.parser_prompts import PARSER_PROMPT
# from Models.response import ParsedInstruction


# class ParserAgent:

#     def __init__(self, llm: LLMService):
#         self.llm = llm

#     def parse(self, instruction: str) -> ParsedInstruction:

#         prompt = PARSER_PROMPT.format(
#             instruction=instruction
#         )

#         response = self.llm.generate(prompt)
        
#         print("===== RAW RESPONSE FROM GEMINI =====")
#         print(response)
#         print("====================================") 
#         parsed = json.loads(response)

#         return ParsedInstruction(**parsed)
    
import json

from Services.llm import LLMService
from Prompts.parser_prompts import PARSER_PROMPT
from Models.response import ParsedInstruction


class ParserAgent:

    def __init__(self, llm: LLMService):
        self.llm = llm

    def parse(self, instruction: str) -> ParsedInstruction:

        prompt = PARSER_PROMPT.format(
            instruction=instruction
        )

        response = self.llm.generate(prompt)

        parsed = json.loads(response)

        return ParsedInstruction(**parsed)
# import json

# from Services.llm import LLMService
# from Prompts.parser_prompts import PARSER_PROMPT
# from Models.response import ParsedInstruction


# class ParserAgent:

#     def __init__(self, llm: LLMService):
#         self.llm = llm

#     def parse(self, instruction: str) -> ParsedInstruction:

#         prompt = f"""
# {PARSER_PROMPT}

# # USER INSTRUCTION

# {instruction}
# """

#         response = self.llm.generate(prompt)

#         print("========== RAW GEMINI RESPONSE ==========")
#         print(response)
#         print("=========================================")

#         parsed = json.loads(response)

#         return ParsedInstruction(**parsed)