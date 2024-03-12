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

@router.get("/test_servicios/prod/consultaDocumento/buscarDocumentoEnExpedientes", tags=["prod","buscarDocumentoEnExpedientes"])
def test_buscarDocumentoEnExpedientes():
    try:
        request = {
            "request": {
            "numeroDocumento": "IF-2021-31350215-GDEBA-TESTGDEBA",
            }
        }
        servicio = ConsultaDocumento(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarDocumentoEnExpedientes(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarDocumentoEnExpedientes",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarDocumentoEnExpedientes",
            "request": request,
            "error": "Request inválido",
            } 