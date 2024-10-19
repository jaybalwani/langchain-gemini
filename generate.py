import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

KEY = os.getenv('GEMINI_API_KEY')


def readPolicy():
    with open('policy.txt', 'r') as file:
        data = file.read().replace('\n', ' ')
    return data

policy = readPolicy()

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=KEY)
prompt = ChatPromptTemplate.from_template("Summarize the following privacy policy in less than 200 words: {policy}?")
chain = prompt | llm | StrOutputParser()

print(chain.invoke({"policy": policy}))
