from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Jaimito Backend")

# Incluir las rutas
app.include_router(router)
