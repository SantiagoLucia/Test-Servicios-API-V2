from fastapi import APIRouter
from servicios.documentosOficiales import DocumentosOficiales
from datetime import datetime
import configparser
from pathlib import Path
from .vincularDocumentosOficialesConNumeroEspecial import test_vincularDocumentosOficialesConNumeroEspecial

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_documentosOficiales"]

router = APIRouter()

@router.get("/test_servicios/prod/documentosOficiales/desvincularDocumentosOficialesConNumeroEspecial", tags=["prod","desvincularDocumentosOficialesConNumeroEspecial"])
def test_desvincularDocumentosOficialesConNumeroEspecial():
    try:
        response_vinculacion = test_vincularDocumentosOficialesConNumeroEspecial()
        numero_expediente = response_vinculacion.get("numeroExpediente")
        numero_documento = "DIFST-2021-9-GDEBA-TESTGDEBA"
        
        request = {
            "request": {
                "usuario": "USERT",
                "numeroExpediente": numero_expediente,
                "documentosOficiales": {
                    "documento": numero_documento,
                }
            }    
        }
        servicio = DocumentosOficiales(uri_servicio, uri_token, auth)
        respuesta = servicio.desvincularDocumentosOficialesConNumeroEspecial(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosOficiales",
            "metodo": "desvincularDocumentosOficialesConNumeroEspecial",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "documentosOficiales",
            "metodo": "desvincularDocumentosOficialesConNumeroEspecial",
            "request": request,
            "error": "Request inválido",
            } 