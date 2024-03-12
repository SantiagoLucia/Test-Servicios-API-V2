from fastapi import APIRouter
from servicios.consultaExpediente import ConsultaExpediente
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaExpediente/buscarExpedientesPorSistemaOrigenUsuario", tags=["prod","buscarExpedientesPorSistemaOrigenUsuario"])
def test_buscarExpedientesPorSistemaOrigenUsuario():
    try:
        request = {"usuario": "USERT"}
        servicio = ConsultaExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarExpedientesPorSistemaOrigenUsuario(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaExpediente",
            "metodo": "buscarExpedientesPorSistemaOrigenUsuario",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaExpediente",
            "metodo": "buscarExpedientesPorSistemaOrigenUsuario",
            "request": request,
            "error": "Request inválido",
            } 