from fastapi import APIRouter
from servicios.consultaEstadoPaseExpediente import ConsultaEstadoPaseExpediente
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaEstadoPaseExpediente"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaEstadoPaseExpediente/consultaEstadoActualExpediente", tags=["prod","consultaEstadoActualExpediente"])
def test_consultaEstadoActualExpediente():
    try:
        request = {"numeroExpediente": "EX-2021-30347340-   -GDEBA-TESTGDEBA"}
        servicio = ConsultaEstadoPaseExpediente(uri_servicio, uri_token, auth)
        respuesta = servicio.consultaEstadoActualExpediente(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaEstadoPaseExpediente",
            "metodo": "consultaEstadoActualExpediente",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaEstadoPaseExpediente",
            "metodo": "consultaEstadoActualExpediente",
            "request": request,
            "error": "Request inválido",
            } 