from fastapi import APIRouter
from servicios.generacionExpediente import GeneracionExpediente
from datetime import datetime
import configparser
import xmltodict
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_generacionExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/generacionExpediente/generarCaratulaExpediente", tags=["prod","generarCaratulaExpediente"])
def test_generarCaratulaExpediente():
    try:
        request = {
            "request": {
                "motivo": "Expediente de prueba. Carece de motivación administrativa.",
                "codigoTrata": "TEST0001",
                "descripcion": "Expediente de prueba. Carece de motivación administrativa.",
                "usuario": "USERT",
                "interno": True,
                "empresa": False,
                "externo": False,
                "persona": True,
                "tieneCuitCuil": False,
            }
        }
        servicio = GeneracionExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.generarCaratulaExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        d = xmltodict.parse(contenido)
        resp_numero = d['soap:Envelope']['soap:Body']['iop:generarCaratulaExpedienteResponse']['return']
        return {
            "servicio": "generacionExpediente",
            "metodo": "generarCaratulaExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numero": resp_numero,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generacionExpediente",
            "metodo": "generarCaratulaExpediente",
            "request": request,
            "error": "Request inválido",
            } 