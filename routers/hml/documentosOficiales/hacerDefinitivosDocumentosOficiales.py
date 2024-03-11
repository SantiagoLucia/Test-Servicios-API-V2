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

@router.get("/test_servicios/hml/documentosOficiales/hacerDefinitivosDocumentosOficiales", tags=["hml","hacerDefinitivosDocumentosOficiales"])
def test_hacerDefinitivosDocumentosOficiales():
    try:
        numero_expediente = test_vincularDocumentosOficiales().get("numeroExpediente")
        
        request = {
            "request": {
                "usuario": "USERT",
                "numeroExpediente": numero_expediente,
            }    
        }
        servicio = DocumentosOficiales(uri_servicio, uri_token, auth)
        respuesta = servicio.hacerDefinitivosDocumentosOficiales(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosOficiales",
            "metodo": "hacerDefinitivosDocumentosOficiales",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "documentosOficiales",
            "metodo": "hacerDefinitivosDocumentosOficiales",
            "request": request,
            "error": "Request inválido",
            } 