from fastapi import APIRouter
from servicios.expedientesAsociados import ExpedientesAsociados
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_expedientesAsociados"]

router = APIRouter()

@router.get("/test_servicios/prod/expedientesAsociados/asociarExpediente", tags=["prod","asociarExpediente"])
def test_asociarExpediente():
    try:
        numero_expediente_1 = test_generarCaratulaExpediente().get("numero")
        numero_expediente_2 = test_generarCaratulaExpediente().get("numero")

        request = {
            "usuario": "USERT",
            "numeroExpediente": numero_expediente_1,
            "numeroExpedienteAsociado": numero_expediente_2,
        }
        
        servicio = ExpedientesAsociados(uri_servicio, uri_token, auth)
        respuesta = servicio.asociarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "expedientesAsociados",
            "metodo": "asociarExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numeroExpedientes": [numero_expediente_1, numero_expediente_2],
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "expedientesAsociados",
            "metodo": "asociarExpediente",
            "request": request,
            "error": "Request inválido",
            } 