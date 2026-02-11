from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate  
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
plantilla = PromptTemplate(input_variables=["nombre"], 
                           template="Saluda al usuario con su nombre, dale una binevenida interesante " \
                           "\nNombre de usuario :{nombre}")
chain = plantilla | llm | StrOutputParser()

#resultado = chain.run(nombre="Fredy")
resultado = chain.invoke({"nombre": "Fredy"})
print(resultado)