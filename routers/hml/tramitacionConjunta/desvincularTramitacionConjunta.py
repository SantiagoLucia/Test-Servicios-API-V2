from fastapi import APIRouter
from servicios.tramitacionConjunta import TramitacionConjunta
from datetime import datetime
import configparser
from pathlib import Path
from .vincularTramitacionConjunta import test_vincularTramitacionConjunta

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_tramitacionConjunta"]

router = APIRouter()

@router.get("/test_servicios/hml/tramitacionConjunta/desvincularTramitacionConjunta", tags=["hml","desvincularTramitacionConjunta"])
def test_desvincularTramitacionConjunta():
    try:
        numero_expediente = test_vincularTramitacionConjunta().get("numeroExpedientePadre")

        request = {
            "usuario": "USERT",
            "numeroExpedientePadre": numero_expediente,
        }
        
        servicio = TramitacionConjunta(uri_servicio, uri_token, auth)
        respuesta = servicio.desvincularTramitacionConjunta(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "tramitacionConjunta",
            "metodo": "desvincularTramitacionConjunta",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "tramitacionConjunta",
            "metodo": "desvincularTramitacionConjunta",
            "request": request,
            "error": "Request inválido",
            } 