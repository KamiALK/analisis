
from fastapi import FastAPI
import analisis.myrequest as function
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from analisis.schemas import *
from fastapi import HTTPException

from fastapi import FastAPI, Request
import requests
'''
uvicorn app:app --host 0.0.0.0 --port 8080
'''
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/obtener_data")
async def obtener_data(request: Request):
    try:
        # Obtener los datos del cuerpo de la solicitud
        data = await request.json()
        print (data)
        # Procesa los datos recibidos y realiza las acciones necesarias
        # Por ejemplo, puedes generar el gráfico de análisis aquí
        
        # Retorna una confirmación de que los datos fueron recibidos y procesados correctamente
        return {"message": "Datos recibidos y procesados correctamente"}
    except Exception as e:
        # Si ocurre algún error, devuelve una respuesta de error con el mensaje correspondiente
        raise HTTPException(status_code=500, detail=f"Error al procesar los datos: {str(e)}")
