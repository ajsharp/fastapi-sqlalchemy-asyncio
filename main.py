from fastapi import FastAPI
from config.utils import execute_query
import asyncio
import random

app = FastAPI()

def exec_query():
    num = random.randint(1, 100)
    query = f'select {num}'
    return execute_query(query)

@app.get("/ping")
async def ping() -> str:
    tasks = [
        exec_query(),
        exec_query(),
        exec_query(),
        exec_query(),
        exec_query(),
        exec_query(),
        exec_query()
    ]
    results = await asyncio.gather(*tasks)

    return "pong"