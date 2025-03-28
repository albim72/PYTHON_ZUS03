from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AddRequest(BaseModel):
    a:float
    b:float

@app.get("/")
def read_root():
    return {"message":"Witaj w prostym API!"}

@app.post("/add")
def add_numbers(request: AddRequest):
    result=request.a + request.b
    return {"result":result}
#uruchomienie -> uvicorn main:app --reload
