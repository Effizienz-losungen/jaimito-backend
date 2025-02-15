from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Jaimito Backend")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Jaimito está en línea"}
