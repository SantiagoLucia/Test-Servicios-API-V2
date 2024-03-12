from fastapi import APIRouter
from servicios.tratas import Tratas
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_tratas"]

router = APIRouter()

@router.get("/test_servicios/prod/tratas/buscarTratasPorCodigo", tags=["prod","buscarTratasPorCodigo"])
def test_buscarTratasPorCodigo():
    try:
        request = {"codigoTrata": "TEST0001"}
        servicio = Tratas(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarTratasPorCodigo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "tratas",
            "metodo": "buscarTratasPorCodigo",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "tratas",
            "metodo": "buscarTratasPorCodigo",
            "request": request,
            "error": "Request inválido",
            } 