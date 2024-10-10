from fastapi import FastAPI, Depends
from typing import Union
from routers.usuarios import rutas_usuarios
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()


async def get_database():
    client = AsyncIOMotorClient("mongodb+srv://usuario1:usuario12345@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority")
    db = client.my_database  # Cambia esto al nombre de tu base de datos
    try:
        yield db
    finally:
        client.close()


#Index
@app.get("/")
async def read_root(db=Depends(get_database)):
    
    usuario = await db.usuarios.find_one({})
    return usuario
    # return {"Iniciado: Ok!"}


app.include_router(rutas_usuarios)
