from fastapi import APIRouter
from servicios.documentosTrabajo import DocumentosTrabajo
from datetime import datetime
import configparser
from pathlib import Path
from ..generacionExpediente.generarCaratulaExpediente import test_generarCaratulaExpediente
import base64

config = configparser.ConfigParser()
config.read(Path("config.ini"))

uri_token = config["prod"]["uri_token"]
auth = (config["prod"]["user"], config["prod"]["pass"])
uri_servicio = config["prod"]["uri_documentosTrabajo"]

router = APIRouter()

@router.get("/test_servicios/prod/documentosTrabajo/adjuntarDocumentosTrabajo", tags=["prod","adjuntarDocumentosTrabajo"])
def test_adjuntarDocumentosTrabajo():
    try:
        numero_expediente = test_generarCaratulaExpediente().get("numero")
        archivo_trabajo = Path(__file__).parents[3] / "static" / "archivo_trabajo.pdf"
        
        with open(archivo_trabajo, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())

        request = {
            "usuario": "USERT",
            "numeroExpediente": numero_expediente,
            "documentosTrabajo": {
                "dataArchivo": encoded_string,
                "nombreArchivo": "archivo_trabajo.pdf",
                "tipoDocumentoTrabajo": "Otros",
            }
        }
        
        servicio = DocumentosTrabajo(uri_servicio, uri_token, auth)
        respuesta = servicio.adjuntarDocumentosTrabajo(request)
        codigo, contenido, tiempo = respuesta
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "servicio": "documentosTrabajo",
            "metodo": "adjuntarDocumentosTrabajo",
            "codigo": codigo,
            "tiempo": tiempo,
            "fecha": dt,
            "numeroExpediente": numero_expediente,
            "request": request,
            "response": contenido,
            }
    except:
        return {
            "servicio": "documentosTrabajo",
            "metodo": "adjuntarDocumentosTrabajo",
            "request": request,
            "error": "Request inválido",
            } 