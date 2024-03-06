from fastapi import APIRouter
from servicios.consultaExpediente import ConsultaExpediente
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_consultaExpediente"]

router = APIRouter()

@router.get("/test_servicios/hml/consultaExpediente/consultarExpedientesPorSistemaOrigenLibreReparticion", tags=["hml","consultarExpedientesPorSistemaOrigenLibreReparticion"])
def test_consultarExpedientesPorSistemaOrigenLibreReparticion():
    try:
        request = {
            "reparticion": "TESTGDEBA",
            "sistemaOrigen": "EE",
        }
        servicio = ConsultaExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.consultarExpedientesPorSistemaOrigenLibreReparticion(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaExpediente",
            "metodo": "consultarExpedientesPorSistemaOrigenLibreReparticion",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaExpediente",
            "metodo": "consultarExpedientesPorSistemaOrigenLibreReparticion",
            "request": request,
            "error": "Request inválido",
            } 