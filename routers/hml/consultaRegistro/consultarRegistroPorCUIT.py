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

@router.get("/test_servicios/hml/consultaRegistro/consultarRegistroPorCUIT", tags=["hml","consultarRegistroPorCUIT"])
def test_consultarRegistroPorCUIT():
    try:
        request = {
            "arg0": {
                "codigoTipoRegistro": "RLSOC0001",
                "cuit": "30900532128",
            }
        }
        servicio = ConsultaRegistro(uri_servicio, uri_token, auth)
        respuesta = servicio.consultarRegistroPorCUIT(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "ConsultaRegistro",
            "metodo": "consultarRegistroPorCUIT",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "ConsultaRegistro",
            "metodo": "consultarRegistroPorCUIT",
            "request": request,
            "error": "Request inválido",
            } 