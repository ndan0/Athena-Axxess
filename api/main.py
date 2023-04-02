import uuid

from models import Persona, Conversation, User, TextCompletionBody
from scripts import speech2text

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from fastapi import FastAPI, UploadFile
import openai


prompt_base = "Your goal is to help your patient with their health needs. You can ask them questions, or you can give them advice. You can also ask them to tell you more about their health history. Do not answer any questions that you do not know the answer to. Do not answer questions irrelevant to health care. Prefer referring a patient to healthcare professionals over providing incorrect information. Be sure to be kind and respectful to your patient."

personas: list[Persona] = [
    Persona(id=1, name="Dr. Cole", prompt="You are Dr. Cole, a fun, caring pediatric doctor.", professional_description="Dr. Cole is a fun, caring pediatric doctor. Use this persona for your younger patients."),
    Persona(id=2, name="Dr. Smith", prompt="You are Dr. Smith, a fun, caring geriatric doctor. Be extra nice, as your patients are elderly and would love to have a conversation. Be sure to constantly reaffirm your love and care for your patient.", professional_description="Dr. Smith is a fun, caring geriatric doctor. Perfect for your older patients."),
]

for persona in personas:
    persona.prompt = f"{persona.prompt} {prompt_base}"

conversations: list[Conversation] = []
users: list[User] = []


app = FastAPI()


@app.get("/")
async def read_root():
    return {"up": True}



@app.get("/persona/list")
async def get_personas() -> list[Persona]:
    return personas


@app.post("/conversation/{conversation_id}/audio")
async def completion_audio(conversation_id: int, file: UploadFile) -> Conversation:
    path = "../assets/" + str(uuid.uuid4()) + ".wav"
    with open(path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    text = speech2text(path)
    return completion_text(conversation_id, text)


@app.post("/conversation/{conversation_id}/text")
async def _completion_text(conversation_id: int, body: TextCompletionBody) -> Conversation:
    return completion_text(conversation_id, body.message)

def completion_text(conversation_id: int, message: str) -> Conversation:
    if conversation_id not in conversations:
        conversation_id = len(conversations)
        conversations.append(Conversation(id=conversation_id, user_id=0, messages=[]))
        
    convo = conversations[conversation_id]
    user = users[convo.user_id]

    msgs = []

    for m in convo.messages:
        msgs.append({
            "role": m.sender,
            "content": m.text
        })

    msgs.append({
        "role": "user",
        "content": message
    })

    completion = openai.ChatCompletion.create(messages=[
        {
            "role": "system",
            "content": user.persona.prompt
        },
        *msgs,
    ], model="gpt-3.5-turbo")
    
    
    msgs.append(completion["choices"][0]["message"]) # type: ignore
    convo.messages = msgs

    return convo