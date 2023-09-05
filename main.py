import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.openapi.utils import get_openapi
from decouple import config


app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "Docker"}

if __name__ == "__main__":
    # $ uvicorn main:app --reload
    port = config("FASTAPI_LOCAL_PORT", cast=int)
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload="True")