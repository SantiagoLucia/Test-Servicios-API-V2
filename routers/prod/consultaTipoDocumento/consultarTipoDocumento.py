from fastapi import APIRouter
from servicios.consultaTipoDocumento import ConsultaTipoDocumento
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaTipoDocumento"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaTipoDocumento/consultarTipoDocumento", tags=["prod","consultarTipoDocumento"])
def test_consultarTipoDocumento():
    try:
        request = {"acronimo": "TESTL"}
        servicio = ConsultaTipoDocumento(uri_servicio, uri_token, auth)
        respuesta = servicio.consultarTipoDocumento(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaTipoDocumento",
            "metodo": "consultarTipoDocumento",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaTipoDocumento",
            "metodo": "consultarTipoDocumento",
            "request": request,
            "error": "Request inválido",
            } 