from fastapi import APIRouter
from servicios.consultaDocumento import ConsultaDocumento
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_consultaDocumento"]

router = APIRouter()

@router.get("/test_servicios/hml/consultaDocumento/buscarPDFPorNumero", tags=["hml","buscarPDFPorNumero"])
def test_buscarPDFPorNumero():
    try:
        request = {
            "request": {
            "assignee": True,
            "numeroDocumento": "IF-2021-00138435-GDEBA-TESTGDEBA",
            "usuarioConsulta": "USERT",
            }
        }
        servicio = ConsultaDocumento(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarPDFPorNumero(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarPDFPorNumero",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "consultaDocumento",
            "metodo": "buscarPDFPorNumero",
            "request": request,
            "error": "Request inválido",
            } 