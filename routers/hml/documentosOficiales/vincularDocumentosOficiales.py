from fastapi import APIRouter
from servicios.documentosOficiales import DocumentosOficiales
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente
from ..generacionDocumentos.generarDocumento import test_generarDocumento

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_documentosOficiales"]

router = APIRouter()

@router.get("/test_servicios/hml/documentosOficiales/vincularDocumentosOficiales", tags=["hml","vincularDocumentosOficiales"])
def test_vincularDocumentosOficiales():
    try:
        numero_expediente = test_generarCaratulaExpediente().get("numero")
        numero_documento = test_generarDocumento().get("numero")
        
        request = {
            "request": {
                "usuario": "USERT",
                "numeroExpediente": numero_expediente,
                "documentosOficiales": numero_documento,
            }
        
        }
        servicio = DocumentosOficiales(uri_servicio, uri_token, auth)
        respuesta = servicio.vincularDocumentosOficiales(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosOficiales",
            "metodo": "vincularDocumentosOficiales",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numeroExpediente": numero_expediente,
            "documentosOficiales": numero_documento,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "documentosOficiales",
            "metodo": "vincularDocumentosOficiales",
            "request": request,
            "error": "Request inválido",
            } 