from fastapi import APIRouter
from servicios.consultaUsuario import ConsultaUsuario
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_consultaUsuario"]

router = APIRouter()

@router.get("/test_servicios/hml/consultaUsuario/buscarPorUsuario", tags=["hml","buscarPorUsuario"])
def test_buscarPorUsuario():
    try:
        request = {"usuario": "SPRIVITERA"}
        servicio = ConsultaUsuario(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarPorUsuario(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaUsuario",
            "metodo": "buscarPorUsuario",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaUsuario",
            "metodo": "buscarPorUsuario",
            "request": request,
            "error": "Request inválido",
            } 