from fastapi import FastAPI
from app.database import Base, engine
from app.router import hello as hello_router
from app.router import users as users_router
from app import model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(hello_router.router)
app.include_router(users_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)