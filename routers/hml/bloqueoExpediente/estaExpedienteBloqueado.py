from fastapi import APIRouter
from servicios.bloqueoExpediente import BloqueoExpediente
from datetime import datetime
import configparser
from pathlib import Path
from .bloquearExpediente import test_bloquearExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_bloqueoExpediente"]

router = APIRouter()

@router.get("/test_servicios/hml/bloqueoExpediente/estaExpedienteBloqueado", tags=["hml","estaExpedienteBloqueado"])
def test_estaExpedienteBloqueado():
    try:
        numero = test_bloquearExpediente().get("numero")
        request = {"numeroExpediente": numero}
        servicio = BloqueoExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.estaExpedienteBloqueado(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "bloqueoExpediente",
            "metodo": "estaExpedienteBloqueado",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "bloqueoExpediente",
            "metodo": "estaExpedienteBloqueado",
            "request": request,
            "error": "Request inválido",
            } 