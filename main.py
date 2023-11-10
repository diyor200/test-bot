from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel

from save_session import start_action

app = FastAPI()

class Data(BaseModel):
    car_number: str
    license_code: str
    license_number: str


@app.post("/")
async def read_root(req: Request):
    data = await req.json()
    msg = await start_action(data)
    return {"message": msg}
