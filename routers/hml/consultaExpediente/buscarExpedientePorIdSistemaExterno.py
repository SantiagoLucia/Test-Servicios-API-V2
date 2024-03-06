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

@router.get("/test_servicios/hml/consultaExpediente/buscarExpedientePorIdSistemaExterno", tags=["hml","buscarExpedientePorIdSistemaExterno"])
def test_buscarExpedientePorIdSistemaExterno():
    try:
        request = {
            "idSistemaExterno": 0,
        }
        servicio = ConsultaExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaExpediente",
            "metodo": "buscarExpedientePorIdSistemaExterno",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaExpediente",
            "metodo": "buscarExpedientePorIdSistemaExterno",
            "request": request,
            "error": "Request inválido",
            } 