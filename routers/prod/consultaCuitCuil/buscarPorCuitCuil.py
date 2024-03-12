from fastapi import APIRouter
from servicios.consultaCuitCuil import ConsultaCuitCuil
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaCuitCuil"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaCuitCuil/buscarPorCuitCuil", tags=["prod","buscarPorCuitCuil"])
def test_buscarPorCuitCuil():
    try:
        request = {"consultaCuitCuilRequest": "20367180162"}
        servicio = ConsultaCuitCuil(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarPorCuitCuil(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaCuitCuil",
            "metodo": "buscarPorCuitCuil",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaCuitCuil",
            "metodo": "buscarPorCuitCuil",
            "request": request,
            "error": "Request inválido",
            } 