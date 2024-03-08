from fastapi import APIRouter
from servicios.generacionPaseExpediente import GeneracionPaseExpediente
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente
from ..generacionDocumentos.generarDocumento import test_generarDocumento

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_generacionPaseExpediente"]

router = APIRouter()

@router.get("/test_servicios/hml/generacionPaseExpediente/generarPaseExpedienteSinDocumento", tags=["hml","generarPaseExpedienteSinDocumento"])
def test_generarPaseExpedienteSinDocumento():
    try:
        numero_expediente = test_generarCaratulaExpediente().get("numero")
        numero_documento = test_generarDocumento().get("numero")
        
        request = {
            "datosPase": {
                "numeroExpediente": numero_expediente,
                "esMesaDestino": False,
                "esReparticionDestino": False,
                "esSectorDestino": False,
                "esUsuarioDestino": True,
                "estadoSeleccionado": "Tramitación",
                "motivoPase": "Expediente de prueba. Carece de motivación administrativa.",
                "usuarioDestino": "USERT",
                "usuarioOrigen": "USERT",
            },
            "numeroGDEBAPase": numero_documento,
        }
        
        servicio = GeneracionPaseExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.generarPaseExpedienteSinDocumento(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpedienteSinDocumento",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generacionPaseExpediente",
            "metodo": "generarPaseExpedienteSinDocumento",
            "request": request,
            "error": "Request inválido",
            } 