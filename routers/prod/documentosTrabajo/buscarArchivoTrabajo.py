from fastapi import APIRouter
from servicios.documentosTrabajo import DocumentosTrabajo
from datetime import datetime
import configparser
from pathlib import Path
from .adjuntarDocumentosTrabajo import test_adjuntarDocumentosTrabajo
import base64

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_documentosTrabajo"]

router = APIRouter()

@router.get("/test_servicios/prod/documentosTrabajo/buscarArchivoTrabajo", tags=["prod","buscarArchivoTrabajo"])
def test_buscarArchivoTrabajo():
    try:
        numero_expediente = test_adjuntarDocumentosTrabajo().get("numeroExpediente")
        request = {
            "usuario": "USERT",
            "numeroExpediente": numero_expediente,
            "nombre": "archivo_trabajo.pdf",
            }
        
        servicio = DocumentosTrabajo(uri_servicio, uri_token, auth)
        respuesta = servicio.buscarArchivoTrabajo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosTrabajo",
            "metodo": "buscarArchivoTrabajo",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "documentosTrabajo",
            "metodo": "buscarArchivoTrabajo",
            "request": request,
            "error": "Request inválido",
            } 