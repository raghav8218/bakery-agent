from pydantic import BaseModel, Field , HttpUrl

class Bakery(BaseModel):
    name:str
    contact: str | None = None
    speciality: str=Field(min_length=1)
    location: str
    source_url: HttpUrl

class BakeryResult(BaseModel):
    city:str
    bakeries: list[Bakery]
    