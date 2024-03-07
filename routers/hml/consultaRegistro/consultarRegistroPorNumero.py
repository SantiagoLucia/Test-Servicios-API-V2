from fastapi import APIRouter
from servicios.consultaRegistro import ConsultaRegistro
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_consultaRegistro"]

router = APIRouter()

@router.get("/test_servicios/hml/consultaRegistro/consultarRegistroPorNumero", tags=["hml","consultarRegistroPorNumero"])
def test_consultarRegistroPorNumero():
    try:
        request = {
            "arg0": {
                "anio": 2021,
                "numero": 23213,
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