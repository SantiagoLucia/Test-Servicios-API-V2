from fastapi import APIRouter
from servicios.datosHistoricos import DatosHistoricos
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_datosHistoricos"]

router = APIRouter()

@router.get("/test_servicios/prod/datosHistoricos/datosHistoricos", tags=["prod","datosHistoricos"])
def test_buscarPorUsuario():
    try:
        request = {
            "request": {
                "numeroRLM": "RL-2021-32086080-GDEBA-DLMJYDHGP",
                "usuario": "USERT",
                #"fecha": "",
            }
        }
        servicio = DatosHistoricos(uri_servicio, uri_token, auth)
        respuesta = servicio.datosHistoricos(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "datosHistoricos",
            "metodo": "datosHistoricos",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "datosHistoricos",
            "metodo": "datosHistoricos",
            "request": request,
            "error": "Request inválido",
            } 