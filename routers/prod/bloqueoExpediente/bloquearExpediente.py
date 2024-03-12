from fastapi import APIRouter
from servicios.bloqueoExpediente import BloqueoExpediente
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_bloqueoExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/bloqueoExpediente/bloquearExpediente", tags=["prod","bloquearExpediente"])
def test_bloquearExpediente():
    try:
        numero = test_generarCaratulaExpediente().get("numero")
        request = {"numeroExpediente": numero}
        servicio = BloqueoExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.bloquearExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "bloqueoExpediente",
            "metodo": "bloquearExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numero": numero,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "bloqueoExpediente",
            "metodo": "bloquearExpediente",
            "request": request,
            "error": "Request inválido",
            } 