from fastapi import FastAPI
from infile import test1

app = FastAPI()
app.include_router(test1.router)

