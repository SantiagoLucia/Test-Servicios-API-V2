from fastapi import APIRouter
from servicios.bloqueoExpediente import BloqueoExpediente
from datetime import datetime
import configparser
from pathlib import Path
from .bloquearExpediente import test_bloquearExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_bloqueoExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/bloqueoExpediente/desbloquearExpediente", tags=["prod","desbloquearExpediente"])
def test_desbloquearExpediente():
    try:
        numero = test_bloquearExpediente().get("numero")
        request = {"numeroExpediente": numero}
        servicio = BloqueoExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.desbloquearExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "bloqueoExpediente",
            "metodo": "desbloquearExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "bloqueoExpediente",
            "metodo": "desbloquearExpediente",
            "request": request,
            "error": "Request inválido",
            } 