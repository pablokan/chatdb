import time
import mesop as me
import mesop.labs as mel
import os

from langchain_community.utilities import SQLDatabase
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv 

load_dotenv()

OPENAI_MODEL = 'gpt-4o-mini' 
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
db = SQLDatabase.from_uri("sqlite:///uni.sqlite")
cadena = SQLDatabaseChain.from_llm(OpenAI(), db)

@me.page(
    path="/",
    title="Mesop Demo Chat",
)
def page():
    mel.chat(transform, title="Gemini Chat", bot_user="Mesop Bot")

generation_config = {
    "temperature": 0.5,
    "top_p": 0.90,
    "top_k": 65,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = llm

def transform(input: str, history: list[mel.ChatMessage]):
    chat_history = "\n".join(message.content for message in history)
    full_input = f"{chat_history}\n{input}"
    response = model.generate_content(full_input, stream=True)
    for chunk in response:
        yield chunk.text
