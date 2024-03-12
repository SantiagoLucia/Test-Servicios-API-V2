from fastapi import APIRouter
from servicios.generacionPaseExpediente import GeneracionPaseExpediente
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_generacionPaseExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/generacionPaseExpediente/generarPaseExpedienteConBloqueo", tags=["prod","generarPaseExpedienteConBloqueo"])
def test_generarPaseExpedienteConBloqueo():
    try:
        numero = test_generarCaratulaExpediente().get("numero")
        
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
        respuesta = servicio.generarPaseExpedienteConBloqueo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpedienteConBloqueo",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpedienteConBloqueo",
            "request": request,
            "error": "Request inválido",
            } 