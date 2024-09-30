import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from fastapi import Depends


async def mongo():
    uri = 'mongodb+srv://usuario1:usuario12345@cluster0.xzwxyov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    client = AsyncIOMotorClient(uri)
    db = client.api_fastapi
    try:
        yield db
    finally:
        client.close()