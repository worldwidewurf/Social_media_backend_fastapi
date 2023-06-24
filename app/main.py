from fastapi import  FastAPI
from .routers import user,post,auth,vote
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .config import settings
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/")
def root():
    return {"message": "Hello World"}

