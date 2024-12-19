from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

from config.cors_config import CorsConfig

load_dotenv()

app = FastAPI()

CorsConfig.middlewareConfig(app)

@app.get("/")
def first_test():
    return {"message": "Data Analysis Test"}

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))