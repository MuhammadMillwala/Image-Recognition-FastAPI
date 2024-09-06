from fastapi import FastAPI
from app.routers import image

app = FastAPI()

app.include_router(image.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Recognition API"}