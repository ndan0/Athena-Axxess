
from enum import Enum
from pydantic import BaseModel


class Sender(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    
class Message(BaseModel):
    id: int
    text: str
    sender: Sender
    timestamp: str

class Persona(BaseModel):
    """
    A persona represents the personality/prompt used for completions. Health professionals can assign their patients to a different persona based on their needs.
    Parameters
    ----------
    id: str
        The unique identifier for the persona.
    name: str
        The name of the persona.
    prompt: str
        The prompt used for completions.
    professional_description: str
        A description of the persona for health professionals. This is used to help health professionals choose the right persona for their patients.
    """
    id: int
    name: str
    prompt: str
    professional_description: str

class Conversation(BaseModel):
    id: int
    user_id: int
    messages: list[Message]


class User(BaseModel):
    id: int
    name: str
    health_history: str
    conversations: list[Conversation]
    persona: Persona

class HealthProfessional(BaseModel):
    id: int
    name: str
    patients: list[User]


class TextCompletionBody(BaseModel):
    message: str