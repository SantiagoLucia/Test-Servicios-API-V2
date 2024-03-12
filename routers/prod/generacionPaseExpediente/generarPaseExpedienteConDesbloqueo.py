from fastapi import APIRouter
from servicios.generacionPaseExpediente import GeneracionPaseExpediente
from datetime import datetime
import configparser
from pathlib import Path
from ..bloqueoExpediente.bloquearExpediente import test_bloquearExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_generacionPaseExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/generacionPaseExpediente/generarPaseExpedienteConDesbloqueo", tags=["prod","generarPaseExpedienteConDesbloqueo"])
def test_generarPaseExpedienteConDesbloqueo():
    try:
        numero = test_bloquearExpediente().get("numero")
        
        request = {
            "datosPase": {
                "numeroExpediente": numero,
                "esMesaDestino": False,
                "esReparticionDestino": False,
                "esSectorDestino": False,
                "esUsuarioDestino": True,
                "estadoSeleccionado": "Tramitación",
                "motivoPase": "Expediente de prueba. Carece de motivación administrativa.",
                "usuarioDestino": "USERT",
                "usuarioOrigen": "USERT",
            }
        }
        
        servicio = GeneracionPaseExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.generarPaseExpedienteConDesbloqueo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpedienteConDesbloqueo",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpedienteConDesbloqueo",
            "request": request,
            "error": "Request inválido",
            } 