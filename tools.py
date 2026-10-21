import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

search=TavilySearch() #not adding maxsearch arg as by default 5

def searchWeb(query:str):
    return search.invoke({"query":query})