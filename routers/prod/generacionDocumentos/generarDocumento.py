from fastapi import APIRouter
from servicios.generacionDocumentos import GeneracionDocumentos
from datetime import datetime
import configparser
import xmltodict
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_generacionDocumentos"]

router = APIRouter()

@router.get("/test_servicios/prod/generacionDocumentos/generarDocumento", tags=["prod","generarDocumento"])
def test_generarDocumento():
    try:
        request = {
            "request": {
                "acronimoTipoDocumento": "TESTL",
                "data": bytes("Documento de prueba. Carece de motivación administrativa.","utf-8"),
                "usuario": "USERT",
                "referencia": "Documento de prueba. Carece de motivación administrativa.",
                "listaUsuariosDestinatariosExternos": {
                    "entry": {
                        "key": "",
                        "value": "",
                    }
                },
                "metaDatos": {
                    "entry": {
                        "key": "",
                        "value": "",
                    }                
                },
            }
        }
        servicio = GeneracionDocumentos(uri_servicio, uri_token, auth)
        respuesta = servicio.generarDocumento(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        d = xmltodict.parse(contenido)
        resp_numero = d['soap:Envelope']['soap:Body']['iop:generarDocumentoResponse']['return']['numero']
        return {
            "servicio": "generacionDocumentos",
            "metodo": "generarDocumento",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numero": resp_numero,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generacionDocumentos",
            "metodo": "generarDocumento",
            "request": request,
            "error": "Request inválido",
            } 