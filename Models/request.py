from pydantic import BaseModel


class UserRequest(BaseModel):
    instruction: str