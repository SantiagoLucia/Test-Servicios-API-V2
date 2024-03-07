from fastapi import APIRouter
from servicios.consultaEstadoPaseExpediente import ConsultaEstadoPaseExpediente
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_consultaEstadoPaseExpediente"]

router = APIRouter()

@router.get("/test_servicios/hml/consultaEstadoPaseExpediente/consultaEstadoActualExpediente", tags=["hml","consultaEstadoActualExpediente"])
def test_consultaEstadoActualExpediente():
    try:
        request = {"numeroExpediente": "EX-2020-00018982- -GDEBA-DDIMJGM"}
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