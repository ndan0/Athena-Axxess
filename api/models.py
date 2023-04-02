
from enum import Enum
from pydantic import BaseModel


class Sender(Enum):
    USER = 1
    PERSONA = 2
    
class Message(BaseModel):
    id: str
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
    id: str
    name: str
    prompt: str
    professional_description: str

class Conversation(BaseModel):
    id: str
    user_id: str
    persona: Persona
    messages: list[Message]


class User(BaseModel):
    id: str
    name: str
    health_history: str
    conversations: list[Conversation]
    persona: Persona

class HealthProfessional(BaseModel):
    id: str
    name: str
    patients: list[User]
