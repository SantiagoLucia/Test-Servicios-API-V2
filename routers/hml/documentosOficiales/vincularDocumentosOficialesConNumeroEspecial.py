from fastapi import APIRouter
from servicios.documentosOficiales import DocumentosOficiales
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_documentosOficiales"]

router = APIRouter()

@router.get("/test_servicios/hml/documentosOficiales/vincularDocumentosOficialesConNumeroEspecial", tags=["hml","vincularDocumentosOficialesConNumeroEspecial"])
def test_vincularDocumentosOficialesConNumeroEspecial():
    try:
        numero_expediente = test_generarCaratulaExpediente().get("numero")
        numero_documento = "DIFST-2021-1-GDEBA-TESTGDEBA"
        
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
        respuesta = servicio.vincularDocumentosOficialesConNumeroEspecial(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosOficiales",
            "metodo": "vincularDocumentosOficialesConNumeroEspecial",
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
            "metodo": "vincularDocumentosOficialesConNumeroEspecial",
            "request": request,
            "error": "Request inválido",
            } 