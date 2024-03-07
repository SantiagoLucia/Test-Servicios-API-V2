from fastapi import APIRouter
from servicios.generacionDocumentos import GeneracionDocumentos
from datetime import datetime
import configparser
import xmltodict
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_generacionDocumentos"]

router = APIRouter()

@router.get("/test_servicios/hml/generacionDocumentos/generarDocumentoUsuarioExterno", tags=["hml","generarDocumentoUsuarioExterno"])
def test_generarDocumentoUsuarioExterno():
    try:
        request = {
            "request": {
                "acronimoTipoDocumento": "TESTL",
                "data": bytes("Documento de prueba. Carece de motivación administrativa.","utf-8"),
                "usuario": "USERT",
                "referencia": "Documento de prueba. Carece de motivación administrativa.",
                "nombreYApellido": "Usuario Test",
                "cargo": "Analista",
                "reparticion": "TESTGDEBA",
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
        respuesta = servicio.generarDocumentoUsuarioExterno(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        d = xmltodict.parse(contenido)
        resp_numero = d['soap:Envelope']['soap:Body']['iop:generarDocumentoUsuarioExternoResponse']['return']['numero']
        return {
            "servicio": "generacionDocumentos",
            "metodo": "generarDocumentoUsuarioExterno",
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
            "metodo": "generarDocumentoUsuarioExterno",
            "request": request,
            "error": "Request inválido",
            } 