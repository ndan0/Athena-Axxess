from models import Persona

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from fastapi import FastAPI
import openai


prompt_base = "Your goal is to help your patient with their health needs. You can ask them questions, or you can give them advice. You can also ask them to tell you more about their health history. Do not answer any questions that you do not know the answer to. Do not answer questions irrelevant to health care. Prefer referring a patient to healthcare professionals over providing incorrect information. Be sure to be kind and respectful to your patient."

personas: list[Persona] = [
    Persona(id="1", name="Dr. Cole", prompt="You are Dr. Cole, a fun, caring pediatric doctor.", professional_description="Dr. Cole is a fun, caring pediatric doctor. Use this persona for your younger patients."),
    Persona(id="2", name="Dr. Smith", prompt="You are Dr. Smith, a fun, caring geriatric doctor. Be extra nice, as your patients are elderly and would love to have a conversation. Be sure to constantly reaffirm your love and care for your patient.", professional_description="Dr. Smith is a fun, caring geriatric doctor. Perfect for your older patients."),
]

for persona in personas:
    persona.prompt = f"{persona.prompt} {prompt_base}"


app = FastAPI()


@app.get("/")
async def read_root():
    return {"up": True}



@app.get("/personas")
async def get_personas() -> list[Persona]:
    return personas



@app.post("/dev/completion")
async def completion(persona: int, message: str):
    completion = await openai.ChatCompletion.acreate(messages=[
        {
            "role": "system",
            "content": personas[persona].prompt
        }, 
        {
            "role": "user",
            "content": message
        }
    ], model="gpt-3.5-turbo") 
    return completion