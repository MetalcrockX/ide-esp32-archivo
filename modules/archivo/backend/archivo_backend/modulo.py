from fastapi import FastAPI
# Import absoluto obligatorio según sus reglas
from archivo_backend.controllers.file_controller import router as file_router

def registrar(app: FastAPI):
    # Registramos tus endpoints bajo la ruta /api/archivo
    app.include_router(file_router, prefix="/api/archivo", tags=["Archivo"])
