from fastapi import APIRouter
from pydantic import BaseModel
import os

router = APIRouter()

class ArchivoData(BaseModel):
    ruta: str
    contenido: str

@router.post("/guardar")
async def guardar_archivo(data: ArchivoData):
    try:
        with open(data.ruta, "w", encoding="utf-8") as f:
            f.write(data.contenido)
        return {"status": "success", "mensaje": "Archivo guardado"}
    except Exception as e:
        return {"status": "error", "mensaje": str(e)}

@router.get("/leer")
async def leer_archivo(ruta: str):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return {"status": "success", "contenido": contenido}
    except Exception as e:
        return {"status": "error", "mensaje": str(e)}
