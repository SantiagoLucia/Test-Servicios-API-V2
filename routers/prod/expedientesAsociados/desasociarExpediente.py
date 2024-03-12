from fastapi import APIRouter
from servicios.expedientesAsociados import ExpedientesAsociados
from datetime import datetime
import configparser
from pathlib import Path
from .asociarExpediente import test_asociarExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_expedientesAsociados"]

router = APIRouter()

@router.get("/test_servicios/prod/expedientesAsociados/desasociarExpediente", tags=["prod","desasociarExpediente"])
def test_desasociarExpediente():
    try:
        numero_expedientes = test_asociarExpediente()["numeroExpedientes"]

        request = {
            "usuario": "USERT",
            "numeroExpediente": numero_expedientes[0],
            "numeroExpedienteDesasociado": numero_expedientes[1],
        }
        
        servicio = ExpedientesAsociados(uri_servicio, uri_token, auth)
        respuesta = servicio.desasociarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "expedientesAsociados",
            "metodo": "desasociarExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "expedientesAsociados",
            "metodo": "desasociarExpediente",
            "request": request,
            "error": "Request inválido",
            } 