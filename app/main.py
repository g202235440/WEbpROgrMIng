from fastapi import FastAPI
from typing import Union
import requests

app = FastAPI()

@app.get("/")
def read_root():
    URL= "https://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000167&pstate=L&redirect=Y"

    contents = requests.get(URL).text

    return {"message": contents}