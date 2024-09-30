from fastapi import APIRouter, Depends
rutas_usuarios = APIRouter()
from dependencias import mongo


@rutas_usuarios.get('/obtener_usuario')
async def obtener_usuario(db=Depends(mongo)):
    usuarios = await db.usuarios.find_one({})
    return usuarios