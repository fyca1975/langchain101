from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate  
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Definición moderna
prompt = PromptTemplate.from_template("Dime un dato curioso sobre {tema}")

# Ejemplo de formateo
prompt_formatted = prompt.format(tema="los pulpos")

chain = prompt | model | StrOutputParser()

print(prompt_formatted)

# 4. Invocar la cadena (Aquí es donde ocurre la magia)
respuesta = chain.invoke({"tema": prompt_formatted })

print(respuesta)
