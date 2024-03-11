from fastapi import APIRouter
from servicios.ffcc import FFCC
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_FFCC"]

router = APIRouter()

@router.get("/test_servicios/hml/ffcc/buscarPorNombre", tags=["hml","buscarPorNombre"])
def test_buscarPorNombre():
    try:
        request = {"nombreFormulario": "FFCC_Nota solicitud trata"}
        servicio = FFCC(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarPorNombre(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "ffcc",
            "metodo": "buscarPorNombre",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "ffcc",
            "metodo": "buscarPorNombre",
            "request": request,
            "error": "Request inválido",
            } 