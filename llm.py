from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from models import BakeryResult

load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    #not adding temperature cuz model doesnt
    #support, for other models #lower for factual n higher val for more creative #usually bw 0 and 2
) 
structuredLLM= llm.with_structured_output(BakeryResult)