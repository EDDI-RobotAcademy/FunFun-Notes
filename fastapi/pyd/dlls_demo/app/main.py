from corsheaders.middleware import CorsMiddleware
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

from config.cors_config import CORSConfig

load_dotenv()

app = FastAPI()

CorsMiddleware.MIDDLEWARECONFIG(APP)

@app.get("/")
def first_test():
    return {"message": "First FastAPI Test"}

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))