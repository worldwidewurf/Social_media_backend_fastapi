from fastapi import  FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Signup(BaseModel):
    
    name: str
    surname: str
    username: str
    email: str
    phone_number: str
    password: str
    confirm_password: str
    
class Login(BaseModel):
    email: str
    password: str
    
    
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/signup")
def signup(signup: Signup):
    print(signup)
    
    return {"message": "Signup Successful"}