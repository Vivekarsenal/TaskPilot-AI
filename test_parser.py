from Services.llm import LLMService
from Agents.parser_agent import ParserAgent

llm = LLMService()

parser = ParserAgent(llm)

result = parser.parse(
    "I want to become a Java Backend Developer in 6 months."
)

print(result)