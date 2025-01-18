from fastapi import FastAPI
import os
import uvicorn

port = os.environ.get("PORT", 8002)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello ~~ from envsat 2"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
