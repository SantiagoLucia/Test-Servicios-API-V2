from fastapi import APIRouter
from servicios.generacionPaseExpediente import GeneracionPaseExpediente
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_generacionPaseExpediente"]

router = APIRouter()

@router.get("/test_servicios/hml/generacionPaseExpediente/generarPaseExpediente", tags=["hml","generarPaseExpediente"])
def test_generarPaseExpediente():
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
        respuesta = servicio.generarPaseExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numero": numero,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpediente",
            "request": request,
            "error": "Request inválido",
            } 