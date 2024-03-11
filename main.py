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
from routers.hml.consultaEstadoPaseExpediente import consultaEstadoActualExpediente as hml_consultaEstadoActualExpediente
from routers.hml.consultaEstadoPaseExpediente import consultaEstadosPaseExpedientePosibles as hml_consultaEstadosPaseExpedientePosibles
from routers.hml.consultaEstadoPaseExpediente import esEstadoPaseExpedienteValido as hml_esEstadoPaseExpedienteValido
from routers.hml.consultaRegistro import consultarRegistroPorCUIT as hml_consultarRegistroPorCUIT
from routers.hml.consultaRegistro import consultarRegistroPorNumero as hml_consultarRegistroPorNumero
from routers.hml.consultaRegistro import listarRegistroPublico as hml_listarRegistroPublico
from routers.hml.consultaRegistro import listarTodosLosRegistrosPublicos as hml_listarTodosLosRegistrosPublicos
from routers.hml.consultarNumero import consultarNumero as hml_consultarNumero
from routers.hml.consultaTipoDocumento import consultarTipoDocumento as hml_consultarTipoDocumento
from routers.hml.datosHistoricos import datosHistoricos as hml_datosHistoricos
from routers.hml.generacionDocumentos import generarDocumento as hml_generarDocumento
from routers.hml.generacionDocumentos import generarDocumentoUsuarioExterno as hml_generarDocumentoUsuarioExterno
from routers.hml.generacionExpediente import generarCaratulaExpediente as hml_generarCaratulaExpediente
from routers.hml.bloqueoExpediente import bloquearExpediente as hml_bloquearExpediente
from routers.hml.bloqueoExpediente import desbloquearExpediente as hml_desbloquearExpediente
from routers.hml.bloqueoExpediente import estaExpedienteBloqueado as hml_estaExpedienteBloqueado
from routers.hml.generacionPaseExpediente import generarPaseExpediente as hml_generarPaseExpediente
from routers.hml.generacionPaseExpediente import generarPaseExpedienteConBloqueo as hml_generarPaseExpedienteConBloqueo
from routers.hml.generacionPaseExpediente import generarPaseExpedienteConDesbloqueo as hml_generarPaseExpedienteConDesbloqueo
from routers.hml.generacionPaseExpediente import generarPaseExpedienteSinDocumento as hml_generarPaseExpedienteSinDocumento
from routers.hml.documentosOficiales import vincularDocumentosOficiales as hml_vincularDocumentosOficiales
from routers.hml.documentosOficiales import desvincularDocumentosOficiales as hml_desvincularDocumentosOficiales
from routers.hml.documentosOficiales import hacerDefinitivosDocumentosOficiales as hml_hacerDefinitivosDocumentosOficiales
from routers.hml.documentosOficiales import eliminarDocumentosOficialesNoDefinitivos as hml_eliminarDocumentosOficialesNoDefinitivos
from routers.hml.documentosOficiales import vincularDocumentosOficialesConNumeroEspecial as hml_vincularDocumentosOficialesConNumeroEspecial
from routers.hml.documentosOficiales import desvincularDocumentosOficialesConNumeroEspecial as hml_desvincularDocumentosOficialesConNumeroEspecial
from routers.hml.documentosTrabajo import adjuntarDocumentosTrabajo as hml_adjuntarDocumentosTrabajo
from routers.hml.documentosTrabajo import buscarArchivoTrabajo as hml_buscarArchivoTrabajo
from routers.hml.documentosTrabajo import desadjuntarDocumentosTrabajo as hml_desadjuntarDocumentosTrabajo
from routers.hml.expedientesAsociados import asociarExpediente as hml_asociarExpediente
from routers.hml.expedientesAsociados import desasociarExpediente as hml_desasociarExpediente

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
app.include_router(hml_consultaEstadoActualExpediente.router)
app.include_router(hml_consultaEstadosPaseExpedientePosibles.router)
app.include_router(hml_esEstadoPaseExpedienteValido.router)
app.include_router(hml_consultarRegistroPorCUIT.router)
app.include_router(hml_consultarRegistroPorNumero.router)
app.include_router(hml_listarRegistroPublico.router)
app.include_router(hml_listarTodosLosRegistrosPublicos.router)
app.include_router(hml_consultarNumero.router)
app.include_router(hml_consultarTipoDocumento.router)
app.include_router(hml_datosHistoricos.router)
app.include_router(hml_generarDocumento.router)
app.include_router(hml_generarDocumentoUsuarioExterno.router)
app.include_router(hml_generarCaratulaExpediente.router)
app.include_router(hml_bloquearExpediente.router)
app.include_router(hml_desbloquearExpediente.router)
app.include_router(hml_estaExpedienteBloqueado.router)
app.include_router(hml_generarPaseExpediente.router)
app.include_router(hml_generarPaseExpedienteConBloqueo.router)
app.include_router(hml_generarPaseExpedienteConDesbloqueo.router)
app.include_router(hml_generarPaseExpedienteSinDocumento.router)
app.include_router(hml_vincularDocumentosOficiales.router)
app.include_router(hml_desvincularDocumentosOficiales.router)
app.include_router(hml_hacerDefinitivosDocumentosOficiales.router)
app.include_router(hml_eliminarDocumentosOficialesNoDefinitivos.router)
app.include_router(hml_vincularDocumentosOficialesConNumeroEspecial.router)
app.include_router(hml_desvincularDocumentosOficialesConNumeroEspecial.router)
app.include_router(hml_adjuntarDocumentosTrabajo.router)
app.include_router(hml_buscarArchivoTrabajo.router)
app.include_router(hml_desadjuntarDocumentosTrabajo.router)
app.include_router(hml_asociarExpediente.router)
app.include_router(hml_desasociarExpediente.router)

@app.get("/test_servicios", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
        }
    )