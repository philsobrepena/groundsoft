from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TelemetryData(BaseModel):
    satellite_id: str
    temperature: float
    humidity:  float

@app.get("/")
def read_root():
    return {"message: ": "Hello, from backend server!"}

@app.post("/telemetry")
async def receive_telemetry(data: TelemetryData):
    print(f"Received!: {data}")
    return {"status": "data rerceived"}
