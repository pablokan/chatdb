# primer éxito en consulta en cristiano a sql !!!!
import a_env_vars
import os
from langchain_community.utilities import SQLDatabase
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY
llm = ChatOpenAI(temperature=0,model_name='gpt-4o-mini')
db = SQLDatabase.from_uri("sqlite:///uni.sqlite")
cadena = SQLDatabaseChain.from_llm(OpenAI(), db)

formato = """
Dada una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

def consulta(input_usuario):
    consu = formato.format(question = input_usuario)
    resultado = cadena.invoke(consu)
    return(resultado)

#c = consulta('Qué edad tiene Javier Ruiz?')
c = consulta('Quienes estudian Ciencias?')
#c = consulta('Quienes estudian Física?')
#c = consulta('Quienes son los profesores de Humanidades?')
print(c)
