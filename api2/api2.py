from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/hc")
def healthcheck():
    return 'API-2 Health - OK'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)