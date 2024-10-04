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

c = cadena.invoke('Cual es el estudiante mas joven? (fecha de nacimiento más reciente)')
#c = consulta('Quienes estudian Ciencias?')
#c = consulta('Quienes estudian Física?')
#c = consulta('Quienes son los profesores de Humanidades?')
print(c)
