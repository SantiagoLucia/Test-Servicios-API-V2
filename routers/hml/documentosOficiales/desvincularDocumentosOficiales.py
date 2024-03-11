from fastapi import APIRouter
from servicios.documentosOficiales import DocumentosOficiales
from datetime import datetime
import configparser
from pathlib import Path
from .vincularDocumentosOficiales import test_vincularDocumentosOficiales

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_documentosOficiales"]

router = APIRouter()

@router.get("/test_servicios/hml/documentosOficiales/desvincularDocumentosOficiales", tags=["hml","desvincularDocumentosOficiales"])
def test_desvincularDocumentosOficiales():
    try:
        response_vinculacion = test_vincularDocumentosOficiales()
        numero_expediente = response_vinculacion.get("numeroExpediente")
        numero_documento = response_vinculacion.get("documentosOficiales")
        
        request = {
            "request": {
                "usuario": "USERT",
                "numeroExpediente": numero_expediente,
                "documentosOficiales": numero_documento,
            }
        
        }
        servicio = DocumentosOficiales(uri_servicio, uri_token, auth)
        respuesta = servicio.desvincularDocumentosOficiales(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosOficiales",
            "metodo": "desvincularDocumentosOficiales",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "documentosOficiales",
            "metodo": "desvincularDocumentosOficiales",
            "request": request,
            "error": "Request inválido",
            } 