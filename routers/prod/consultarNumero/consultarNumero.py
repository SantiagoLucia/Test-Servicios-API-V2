from fastapi import APIRouter
from servicios.consultarNumero import ConsultarNumero
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultarNumero"]

router = APIRouter()

@router.get("/test_servicios/prod/consultarNumero/consultarNumero", tags=["prod","consultarNumero"])
def test_consultarNumero():
    try:
        request = {
            "anio": 2022,
            "numero": 1,
        }
        servicio = ConsultarNumero(uri_servicio, uri_token, auth)
        respuesta = servicio.consultarNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "ConsultarNumero",
            "metodo": "consultarNumero",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "ConsultarNumero",
            "metodo": "consultarNumero",
            "request": request,
            "error": "Request inválido",
            } 