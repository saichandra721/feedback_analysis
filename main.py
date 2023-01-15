from fastapi import FastAPI

import models
from database import engine
from routers import authentication, faculty, student

app = FastAPI()
models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(faculty.router)
app.include_router(student.router)


@app.get('/')
def home():
    return {'Have a great day'}