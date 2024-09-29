from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    
    if(2 >= 1):
        print("olamundo")
    
        
    return {"Jalando: 1"}

