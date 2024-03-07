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

@router.get("/test_servicios/hml/consultaRegistro/listarTodosLosRegistrosPublicos", tags=["hml","listarTodosLosRegistrosPublicos"])
def test_listarTodosLosRegistrosPublicos():
    try:
        request = {}
        servicio = ConsultaRegistro(uri_servicio, uri_token, auth)
        respuesta = servicio.listarTodosLosRegistrosPublicos(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "ConsultaRegistro",
            "metodo": "listarTodosLosRegistrosPublicos",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "ConsultaRegistro",
            "metodo": "listarTodosLosRegistrosPublicos",
            "request": request,
            "error": "Request inválido",
            } 