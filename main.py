from tools import searchWeb
from llm import structuredLLM



city= input("enter a city: ")

search_res= searchWeb(
    f"popular bakeries in {city} India contacts details specialities"
)

prompt= f"""find popular bakeries in {city} India using the search results below
for each bakery,
-include its name 
-include its contact details (publically available), if not avail, then none,
-write a one -two sentence short summary of whats special
-include a source url supporting the info 
-location
dont put fake data or made up contacts or specialities

search results: {search_res}

"""

response=structuredLLM.invoke(prompt)


print(f"popular bakeries in {city}: \n")

for bakery in response.bakeries:
    print(f"Name:{bakery.name}")
    print(f"Contact: {bakery.contact or 'Not found'}")
    print(f"Speciality: {bakery.speciality}")
    print(f"Location:{bakery.location} " )
    print(f"Source: {bakery.source_url}")
    
    print("-" * 40)