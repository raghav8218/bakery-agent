import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

search=TavilySearch(max_results=5) #maxres arg as for 5 res 

def searchWeb(query:str):
    response= search.invoke({"query":query})
    return [
        {
            'title':result['title'],
            'url':result['url'],
            'content':result['content']
            }
        for result in response['results']
        
    ]
    