import os

from langchain_community.utilities import SQLDatabase
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv 
import mesop as me
import mesop.labs as mel
from mesop import stateclass

load_dotenv()
OPENAI_MODEL = 'gpt-4o-mini' 
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
db = SQLDatabase.from_uri("sqlite:///uni.sqlite")
cadena = SQLDatabaseChain.from_llm(OpenAI(), db)

@stateclass
class State:
    pass

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/",
    title="Mesop Demo Chat",
)
def page():
    mel.chat(transform, title="LangChain Chat", bot_user="Mesop Bot")

def transform(input: str, history: list[mel.ChatMessage]):
    messages = [f"System: You are a helpful assistant."]
    messages.extend([f"User: {message.content}" for message in history])
    messages.append(f"User: {input}")

    query = "\n".join(messages)
    resp = llm.stream(query)
    
    for chunk in resp:
        if chunk:
            yield chunk