from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from routers.hml.consultaUsuario import buscarPorUsuario as hml_buscarPorUsuario
from routers.hml.consultaDocumento import buscarDetallePorNumero as hml_buscarDetallePorNumero
from routers.hml.consultaDocumento import buscarDocumentoEnExpedientes as hml_buscarDocumentoEnExpedientes
from routers.hml.consultaDocumento import buscarDocumentoPublicablePorNumero as hml_buscarDocumentoPublicablePorNumero
from routers.hml.consultaDocumento import buscarNumeroGDEBA as hml_buscarNumeroGDEBA
from routers.hml.consultaDocumento import buscarPDFPorNumero as hml_buscarPDFPorNumero
from routers.hml.consultaDocumento import buscarPorNumero as hml_buscarPorNumero
from routers.hml.consultaCuitCuil import buscarPorCuitCuil as hml_buscarPorCuitCuil
from routers.hml.consultaExpediente import buscarCaratulaPorNumeroExpediente as hml_buscarCaratulaPorNumeroExpediente
from routers.hml.consultaExpediente import buscarCodigoCaratulaPorNumeroExpediente as hml_buscarCodigoCaratulaPorNumeroExpediente
from routers.hml.consultaExpediente import buscarDatosExpedientePorCodigosTrata as hml_buscarDatosExpedientePorCodigosTrata
from routers.hml.consultaExpediente import buscarDatosExpedienteVariable as hml_buscarDatosExpedienteVariable
from routers.hml.consultaExpediente import buscarExpediente as hml_buscarExpediente
from routers.hml.consultaExpediente import buscarExpedientePorIdSistemaExterno as hml_buscarExpedientePorIdSistemaExterno
from routers.hml.consultaExpediente import buscarExpedientesPorSistemaOrigenLibreUsuario as hml_buscarExpedientesPorSistemaOrigenLibreUsuario
from routers.hml.consultaExpediente import buscarExpedientesPorSistemaOrigenUsuario as hml_buscarExpedientesPorSistemaOrigenUsuario
from routers.hml.consultaExpediente import buscarHistorialPasesExpediente as hml_buscarHistorialPasesExpediente
from routers.hml.consultaExpediente import consultarCaratulaVariablePorNumeroExpedienteUsuario as hml_consultarCaratulaVariablePorNumeroExpedienteUsuario
from routers.hml.consultaExpediente import consultarExpedienteDetallado as hml_consultarExpedienteDetallado
from routers.hml.consultaExpediente import consultarExpedientesPorSistemaOrigenLibreReparticion as hml_consultarExpedientesPorSistemaOrigenLibreReparticion
from routers.hml.consultaExpediente import consultarExpedientesPorSistemaOrigenReparticion as hml_consultarExpedientesPorSistemaOrigenReparticion
from routers.hml.consultaExpediente import consultarIdFCPorNumeroExpediente as hml_consultarIdFCPorNumeroExpediente
from routers.hml.consultaExpediente import validarExpediente as hml_validarExpediente

import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(hml_buscarPorUsuario.router)
app.include_router(hml_buscarDetallePorNumero.router)
app.include_router(hml_buscarDocumentoEnExpedientes.router)
app.include_router(hml_buscarDocumentoPublicablePorNumero.router)
app.include_router(hml_buscarNumeroGDEBA.router)
app.include_router(hml_buscarPDFPorNumero.router)
app.include_router(hml_buscarPorNumero.router)
app.include_router(hml_buscarPorCuitCuil.router)
app.include_router(hml_buscarCaratulaPorNumeroExpediente.router)
app.include_router(hml_buscarCodigoCaratulaPorNumeroExpediente.router)
app.include_router(hml_buscarDatosExpedientePorCodigosTrata.router)
app.include_router(hml_buscarDatosExpedienteVariable.router)
app.include_router(hml_buscarExpediente.router)
app.include_router(hml_buscarExpedientePorIdSistemaExterno.router)
app.include_router(hml_buscarExpedientesPorSistemaOrigenLibreUsuario.router)
app.include_router(hml_buscarExpedientesPorSistemaOrigenUsuario.router)
app.include_router(hml_buscarHistorialPasesExpediente.router)
app.include_router(hml_consultarCaratulaVariablePorNumeroExpedienteUsuario.router)
app.include_router(hml_consultarExpedienteDetallado.router)
app.include_router(hml_consultarExpedientesPorSistemaOrigenLibreReparticion.router)
app.include_router(hml_consultarExpedientesPorSistemaOrigenReparticion.router)
app.include_router(hml_consultarIdFCPorNumeroExpediente.router)
app.include_router(hml_validarExpediente.router)

@app.get("/test_servicios", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
        }
    )