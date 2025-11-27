import json
import asyncio

from fastapi import FastAPI
from app.api.generate.function_model import generateESGreport, generatePolicy, generateESGreportNew


app = FastAPI()

app.include_router(generateESGreport)