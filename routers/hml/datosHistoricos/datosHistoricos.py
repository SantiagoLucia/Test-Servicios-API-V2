from fastapi import APIRouter
from servicios.datosHistoricos import DatosHistoricos
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_datosHistoricos"]

router = APIRouter()

@router.get("/test_servicios/hml/datosHistoricos/datosHistoricos", tags=["hml","datosHistoricos"])
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