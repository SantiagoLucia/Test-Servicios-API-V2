from fastapi import APIRouter
from servicios.consultaDocumento import ConsultaDocumento
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_consultaDocumento"]

router = APIRouter()

@router.get("/test_servicios/hml/consultaDocumento/buscarNumeroGDEBA", tags=["hml","buscarNumeroGDEBA"])
def test_buscarNumeroGDEBA():
    try:
        request = {
            "request": {
            "id": "procesoGEDO.439390192",
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