from Services.llm import LLMService 

llm = LLMService()

response = llm.generate("Tell me a fun fact about space.")

print(response)