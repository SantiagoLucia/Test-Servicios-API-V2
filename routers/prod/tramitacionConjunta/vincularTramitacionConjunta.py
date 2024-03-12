from fastapi import APIRouter
from servicios.tramitacionConjunta import TramitacionConjunta
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionPaseExpediente.generarPaseExpediente import test_generarPaseExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_tramitacionConjunta"]

router = APIRouter()

@router.get("/test_servicios/prod/tramitacionConjunta/vincularTramitacionConjunta", tags=["prod","vincularTramitacionConjunta"])
def test_vincularTramitacionConjunta():
    try:
        numero_expediente_1 = test_generarPaseExpediente().get("numero")
        numero_expediente_2 = test_generarPaseExpediente().get("numero")

        request = {
            "usuario": "USERT",
            "numeroExpedientePadre": numero_expediente_1,
            "expedientesHijo": numero_expediente_2,
        }
        
        servicio = TramitacionConjunta(uri_servicio, uri_token, auth)
        respuesta = servicio.vincularTramitacionConjunta(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "tramitacionConjunta",
            "metodo": "vincularTramitacionConjunta",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numeroExpedientePadre": numero_expediente_1,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "tramitacionConjunta",
            "metodo": "vincularTramitacionConjunta",
            "request": request,
            "error": "Request inválido",
            } 