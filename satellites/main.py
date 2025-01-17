from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SatteliteData(BaseModel):
    satellite_id: str
    temperature: float
    humidity: float

@app.post("/sat/1")
async def receive_sat1_data(data: SatteliteData):
    print(f"Received Data From Satellite 1!: {data}")
    return {"status": "data received"}
