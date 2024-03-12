from fastapi import APIRouter
from servicios.consultaDocumento import ConsultaDocumento
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaDocumento"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaDocumento/buscarDetallePorNumero", tags=["prod","buscarDetallePorNumero"])
def test_buscarDetallePorNumero():
    try:
        request = {
            "request": {
            "assignee": True,
            "numeroDocumento": "IF-2021-31350215-GDEBA-TESTGDEBA",
            "usuarioConsulta": "USERT",
            }
        }
        servicio = ConsultaDocumento(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarDetallePorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarDetallePorNumero",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarDetallePorNumero",
            "request": request,
            "error": "Request inválido",
            } 