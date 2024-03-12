from fastapi import APIRouter
from servicios.consultaDocumento import ConsultaDocumento
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaDocumento"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaDocumento/buscarNumeroGDEBA", tags=["prod","buscarNumeroGDEBA"])
def test_buscarNumeroGDEBA():
    try:
        request = {
            "request": {
            "id": "procesoGEDO.1744335941",
            }
        }
        servicio = ConsultaDocumento(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarNumeroGDEBA(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarNumeroGDEBA",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarNumeroGDEBA",
            "request": request,
            "error": "Request inválido",
            } 