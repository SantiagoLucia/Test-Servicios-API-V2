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

@router.get("/test_servicios/hml/consultaExpediente/buscarDatosExpedientePorCodigosTrata", tags=["hml","buscarDatosExpedientePorCodigosTrata"])
def test_buscarDatosExpedientePorCodigosTrata():
    try:
        request = {
            "codigosTrata": "TEST0001",
            "estadoDestino": "Tramitación",
            "usuario": "USERT",
        }
        servicio = ConsultaExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarDatosExpedientePorCodigosTrata(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaExpediente",
            "metodo": "buscarDatosExpedientePorCodigosTrata",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaExpediente",
            "metodo": "buscarDatosExpedientePorCodigosTrata",
            "request": request,
            "error": "Request inválido",
            } 