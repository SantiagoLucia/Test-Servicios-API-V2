from fastapi import APIRouter
from servicios.consultaRegistro import ConsultaRegistro
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_consultaRegistro"]

router = APIRouter()

@router.get("/test_servicios/prod/consultaRegistro/consultarRegistroPorNumero", tags=["prod","consultarRegistroPorNumero"])
def test_consultarRegistroPorNumero():
    try:
        request = {
            "arg0": {
                "anio": 2021,
                "numero": 19967403,
            }
        }
        servicio = ConsultaRegistro(uri_servicio, uri_token, auth)
        respuesta = servicio.consultarRegistroPorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "ConsultaRegistro",
            "metodo": "consultarRegistroPorNumero",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "ConsultaRegistro",
            "metodo": "consultarRegistroPorNumero",
            "request": request,
            "error": "Request inválido",
            } 