# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()


# class LLMService:

#     def __init__(self):
#         api_key = os.getenv("GEMINI_API_KEY")
        
#         print("Using API Key:", api_key[:10] + "...")
#         if not api_key:
#             raise ValueError(
#                 "GEMINI_API_KEY is missing! Make sure it is defined in your .env file."
#             )

#         self.client = genai.Client(api_key=api_key)

#     def generate(self, prompt: str) -> str:

#         response = self.client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=prompt
#         )

#         return response.text

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

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing!")

        self.client = Groq(api_key=api_key)

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content