from fastapi import APIRouter
from servicios.generarTareaGEDO import GenerarTareaGEDO
from datetime import datetime
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["hml"]["uri_token"]
auth = (config["hml"]["user"], config["hml"]["pass"])
uri_servicio = config["hml"]["uri_generarTareaGEDO"]

router = APIRouter()

@router.get("/test_servicios/hml/generarTareaGEDO/generarTareaGEDO", tags=["hml","generarTareaGEDO"])
def test_generarTareaGEDO():
    try:
        request = {
            "request": {
                "acronimoTipoDocumento": "TESTL",
                "data": bytes("Documento de prueba. Carece de motivación administrativa.","utf-8"),
                "tarea": "Firmar Documento",
                "usuarioEmisor": "USERT",
                "usuarioFirmante": {
                    "entry": {
                        "key": 1,
                        "value": "USERT",
                    }                
                },
                "usuarioReceptor": "USERT",
                "referencia": "Documento de prueba. Carece de motivación administrativa.",
                "suscribirseAlDocumento": True,
                "enviarCorreoReceptor": False,
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
                "recibirAvisoFirma": False
            }
        }
        servicio = GenerarTareaGEDO(uri_servicio, uri_token, auth)
        respuesta = servicio.generarTareaGEDO(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "generarTareaGEDO",
            "metodo": "generarTareaGEDO",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "generarTareaGEDO",
            "metodo": "generarTareaGEDO",
            "request": request,
            "error": "Request inválido",
            } 