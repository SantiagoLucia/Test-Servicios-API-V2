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

@router.get("/test_servicios/prod/consultaRegistro/consultarRegistroPorCUIT", tags=["prod","consultarRegistroPorCUIT"])
def test_consultarRegistroPorCUIT():
    try:
        request = {
            "arg0": {
                "codigoTipoRegistro": "RLSOC0001",
                "cuit": "30717410439",
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