from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database import myclient, get_db

class User(BaseModel):
    email: str
    password: str


app = FastAPI()
db = get_db()

origins = [
    'http://127.0.0.1:5500'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Hello, World!"}


@app.post('/sign_up/')
async def sign_up(login_credentials: User):
    db.insert_one({
        'email': login_credentials.email,
        'password': login_credentials.password
    })

    return {"details": login_credentials}


@app.post('/login_in/')
async def login_in(signup_credentials: User):
    db.insert_one({
        'email': signup_credentials.email,
        'password': signup_credentials.password
    })

    return {"details": signup_credentials}


@app.delete('/users/delete/')
async def delete_user(email: str):
    db.delete_one({
        'email': email
    })

    return {"message": "User data deleted succesfully"}