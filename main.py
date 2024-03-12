from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# HML
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
from routers.hml.ffcc import buscarPorNombre as hml_buscarPorNombre
from routers.hml.generarTareaGEDO import generarTareaGEDO as hml_generarTareaGEDO
from routers.hml.tramitacionConjunta import vincularTramitacionConjunta as hml_vincularTramitacionConjunta
from routers.hml.tramitacionConjunta import desvincularTramitacionConjunta as hml_desvincularTramitacionConjunta
from routers.hml.tratas import buscarTratasPorCodigo as hml_buscarTratasPorCodigo

# PROD
from routers.prod.consultaUsuario import buscarPorUsuario as prod_buscarPorUsuario
from routers.prod.consultaDocumento import buscarDetallePorNumero as prod_buscarDetallePorNumero
from routers.prod.consultaDocumento import buscarDocumentoEnExpedientes as prod_buscarDocumentoEnExpedientes
from routers.prod.consultaDocumento import buscarDocumentoPublicablePorNumero as prod_buscarDocumentoPublicablePorNumero
from routers.prod.consultaDocumento import buscarNumeroGDEBA as prod_buscarNumeroGDEBA
from routers.prod.consultaDocumento import buscarPDFPorNumero as prod_buscarPDFPorNumero
from routers.prod.consultaDocumento import buscarPorNumero as prod_buscarPorNumero
from routers.prod.consultaCuitCuil import buscarPorCuitCuil as prod_buscarPorCuitCuil
from routers.prod.consultaExpediente import buscarCaratulaPorNumeroExpediente as prod_buscarCaratulaPorNumeroExpediente
from routers.prod.consultaExpediente import buscarCodigoCaratulaPorNumeroExpediente as prod_buscarCodigoCaratulaPorNumeroExpediente
from routers.prod.consultaExpediente import buscarDatosExpedientePorCodigosTrata as prod_buscarDatosExpedientePorCodigosTrata
from routers.prod.consultaExpediente import buscarDatosExpedienteVariable as prod_buscarDatosExpedienteVariable
from routers.prod.consultaExpediente import buscarExpediente as prod_buscarExpediente
from routers.prod.consultaExpediente import buscarExpedientePorIdSistemaExterno as prod_buscarExpedientePorIdSistemaExterno
from routers.prod.consultaExpediente import buscarExpedientesPorSistemaOrigenLibreUsuario as prod_buscarExpedientesPorSistemaOrigenLibreUsuario
from routers.prod.consultaExpediente import buscarExpedientesPorSistemaOrigenUsuario as prod_buscarExpedientesPorSistemaOrigenUsuario
from routers.prod.consultaExpediente import buscarHistorialPasesExpediente as prod_buscarHistorialPasesExpediente
from routers.prod.consultaExpediente import consultarCaratulaVariablePorNumeroExpedienteUsuario as prod_consultarCaratulaVariablePorNumeroExpedienteUsuario
from routers.prod.consultaExpediente import consultarExpedienteDetallado as prod_consultarExpedienteDetallado
from routers.prod.consultaExpediente import consultarExpedientesPorSistemaOrigenLibreReparticion as prod_consultarExpedientesPorSistemaOrigenLibreReparticion
from routers.prod.consultaExpediente import consultarExpedientesPorSistemaOrigenReparticion as prod_consultarExpedientesPorSistemaOrigenReparticion
from routers.prod.consultaExpediente import consultarIdFCPorNumeroExpediente as prod_consultarIdFCPorNumeroExpediente
from routers.prod.consultaExpediente import validarExpediente as prod_validarExpediente
from routers.prod.consultaEstadoPaseExpediente import consultaEstadoActualExpediente as prod_consultaEstadoActualExpediente
from routers.prod.consultaEstadoPaseExpediente import consultaEstadosPaseExpedientePosibles as prod_consultaEstadosPaseExpedientePosibles
from routers.prod.consultaEstadoPaseExpediente import esEstadoPaseExpedienteValido as prod_esEstadoPaseExpedienteValido
from routers.prod.consultaRegistro import consultarRegistroPorCUIT as prod_consultarRegistroPorCUIT
from routers.prod.consultaRegistro import consultarRegistroPorNumero as prod_consultarRegistroPorNumero
from routers.prod.consultaRegistro import listarRegistroPublico as prod_listarRegistroPublico
from routers.prod.consultaRegistro import listarTodosLosRegistrosPublicos as prod_listarTodosLosRegistrosPublicos
from routers.prod.consultarNumero import consultarNumero as prod_consultarNumero
from routers.prod.consultaTipoDocumento import consultarTipoDocumento as prod_consultarTipoDocumento
from routers.prod.datosHistoricos import datosHistoricos as prod_datosHistoricos
from routers.prod.generacionDocumentos import generarDocumento as prod_generarDocumento
from routers.prod.generacionDocumentos import generarDocumentoUsuarioExterno as prod_generarDocumentoUsuarioExterno
from routers.prod.generacionExpediente import generarCaratulaExpediente as prod_generarCaratulaExpediente
from routers.prod.bloqueoExpediente import bloquearExpediente as prod_bloquearExpediente
from routers.prod.bloqueoExpediente import desbloquearExpediente as prod_desbloquearExpediente
from routers.prod.bloqueoExpediente import estaExpedienteBloqueado as prod_estaExpedienteBloqueado
from routers.prod.generacionPaseExpediente import generarPaseExpediente as prod_generarPaseExpediente
from routers.prod.generacionPaseExpediente import generarPaseExpedienteConBloqueo as prod_generarPaseExpedienteConBloqueo
from routers.prod.generacionPaseExpediente import generarPaseExpedienteConDesbloqueo as prod_generarPaseExpedienteConDesbloqueo
from routers.prod.generacionPaseExpediente import generarPaseExpedienteSinDocumento as prod_generarPaseExpedienteSinDocumento
from routers.prod.documentosOficiales import vincularDocumentosOficiales as prod_vincularDocumentosOficiales
from routers.prod.documentosOficiales import desvincularDocumentosOficiales as prod_desvincularDocumentosOficiales
from routers.prod.documentosOficiales import hacerDefinitivosDocumentosOficiales as prod_hacerDefinitivosDocumentosOficiales
from routers.prod.documentosOficiales import eliminarDocumentosOficialesNoDefinitivos as prod_eliminarDocumentosOficialesNoDefinitivos
from routers.prod.documentosOficiales import vincularDocumentosOficialesConNumeroEspecial as prod_vincularDocumentosOficialesConNumeroEspecial
from routers.prod.documentosOficiales import desvincularDocumentosOficialesConNumeroEspecial as prod_desvincularDocumentosOficialesConNumeroEspecial
from routers.prod.documentosTrabajo import adjuntarDocumentosTrabajo as prod_adjuntarDocumentosTrabajo
from routers.prod.documentosTrabajo import buscarArchivoTrabajo as prod_buscarArchivoTrabajo
from routers.prod.documentosTrabajo import desadjuntarDocumentosTrabajo as prod_desadjuntarDocumentosTrabajo
from routers.prod.expedientesAsociados import asociarExpediente as prod_asociarExpediente
from routers.prod.expedientesAsociados import desasociarExpediente as prod_desasociarExpediente
from routers.prod.ffcc import buscarPorNombre as prod_buscarPorNombre
from routers.prod.generarTareaGEDO import generarTareaGEDO as prod_generarTareaGEDO
from routers.prod.tramitacionConjunta import vincularTramitacionConjunta as prod_vincularTramitacionConjunta
from routers.prod.tramitacionConjunta import desvincularTramitacionConjunta as prod_desvincularTramitacionConjunta
from routers.prod.tratas import buscarTratasPorCodigo as prod_buscarTratasPorCodigo


import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path("config.ini"))

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# HML
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
app.include_router(hml_buscarPorNombre.router)
app.include_router(hml_generarTareaGEDO.router)
app.include_router(hml_vincularTramitacionConjunta.router)
app.include_router(hml_desvincularTramitacionConjunta.router)
app.include_router(hml_buscarTratasPorCodigo.router)

# PROD
app.include_router(prod_buscarPorUsuario.router)
app.include_router(prod_buscarDetallePorNumero.router)
app.include_router(prod_buscarDocumentoEnExpedientes.router)
app.include_router(prod_buscarDocumentoPublicablePorNumero.router)
app.include_router(prod_buscarNumeroGDEBA.router)
app.include_router(prod_buscarPDFPorNumero.router)
app.include_router(prod_buscarPorNumero.router)
app.include_router(prod_buscarPorCuitCuil.router)
app.include_router(prod_buscarCaratulaPorNumeroExpediente.router)
app.include_router(prod_buscarCodigoCaratulaPorNumeroExpediente.router)
app.include_router(prod_buscarDatosExpedientePorCodigosTrata.router)
app.include_router(prod_buscarDatosExpedienteVariable.router)
app.include_router(prod_buscarExpediente.router)
app.include_router(prod_buscarExpedientePorIdSistemaExterno.router)
app.include_router(prod_buscarExpedientesPorSistemaOrigenLibreUsuario.router)
app.include_router(prod_buscarExpedientesPorSistemaOrigenUsuario.router)
app.include_router(prod_buscarHistorialPasesExpediente.router)
app.include_router(prod_consultarCaratulaVariablePorNumeroExpedienteUsuario.router)
app.include_router(prod_consultarExpedienteDetallado.router)
app.include_router(prod_consultarExpedientesPorSistemaOrigenLibreReparticion.router)
app.include_router(prod_consultarExpedientesPorSistemaOrigenReparticion.router)
app.include_router(prod_consultarIdFCPorNumeroExpediente.router)
app.include_router(prod_validarExpediente.router)
app.include_router(prod_consultaEstadoActualExpediente.router)
app.include_router(prod_consultaEstadosPaseExpedientePosibles.router)
app.include_router(prod_esEstadoPaseExpedienteValido.router)
app.include_router(prod_consultarRegistroPorCUIT.router)
app.include_router(prod_consultarRegistroPorNumero.router)
app.include_router(prod_listarRegistroPublico.router)
app.include_router(prod_listarTodosLosRegistrosPublicos.router)
app.include_router(prod_consultarNumero.router)
app.include_router(prod_consultarTipoDocumento.router)
app.include_router(prod_datosHistoricos.router)
app.include_router(prod_generarDocumento.router)
app.include_router(prod_generarDocumentoUsuarioExterno.router)
app.include_router(prod_generarCaratulaExpediente.router)
app.include_router(prod_bloquearExpediente.router)
app.include_router(prod_desbloquearExpediente.router)
app.include_router(prod_estaExpedienteBloqueado.router)
app.include_router(prod_generarPaseExpediente.router)
app.include_router(prod_generarPaseExpedienteConBloqueo.router)
app.include_router(prod_generarPaseExpedienteConDesbloqueo.router)
app.include_router(prod_generarPaseExpedienteSinDocumento.router)
app.include_router(prod_vincularDocumentosOficiales.router)
app.include_router(prod_desvincularDocumentosOficiales.router)
app.include_router(prod_hacerDefinitivosDocumentosOficiales.router)
app.include_router(prod_eliminarDocumentosOficialesNoDefinitivos.router)
app.include_router(prod_vincularDocumentosOficialesConNumeroEspecial.router)
app.include_router(prod_desvincularDocumentosOficialesConNumeroEspecial.router)
app.include_router(prod_adjuntarDocumentosTrabajo.router)
app.include_router(prod_buscarArchivoTrabajo.router)
app.include_router(prod_desadjuntarDocumentosTrabajo.router)
app.include_router(prod_asociarExpediente.router)
app.include_router(prod_desasociarExpediente.router)
app.include_router(prod_buscarPorNombre.router)
app.include_router(prod_generarTareaGEDO.router)
app.include_router(prod_vincularTramitacionConjunta.router)
app.include_router(prod_desvincularTramitacionConjunta.router)
app.include_router(prod_buscarTratasPorCodigo.router)


dic_metodos = {
    "bloqueoExpediente": [
        "bloquearExpediente",
        "desbloquearExpediente",
        "estaExpedienteBloqueado"
        ],
    "consultaCuitCuil": [
        "buscarPorCuitCuil"
        ],
    "consultaDocumento": [
        "buscarDetallePorNumero",
        "buscarDocumentoEnExpedientes",
        "buscarDocumentoPublicablePorNumero",
        "buscarNumeroGDEBA",
        "buscarPDFPorNumero",
        "buscarPorNumero"
        ],
    "consultaEstadoPaseExpediente": [
        "consultaEstadoActualExpediente",
        "consultaEstadosPaseExpedientePosibles",
        "esEstadoPaseExpedienteValido"
        ],
    "consultaExpediente": [
        "buscarCaratulaPorNumeroExpediente",
        "buscarCodigoCaratulaPorNumeroExpediente",
        "buscarDatosExpedientePorCodigosTrata",
        "buscarDatosExpedienteVariable",
        "buscarExpediente",
        "buscarExpedientePorIdSistemaExterno",
        "buscarExpedientesPorSistemaOrigenLibreUsuario",
        "buscarExpedientesPorSistemaOrigenUsuario",
        "buscarHistorialPasesExpediente",
        "consultarCaratulaVariablePorNumeroExpedienteUsuario",
        "consultarExpedienteDetallado",
        "consultarExpedientesPorSistemaOrigenLibreReparticion",
        "consultarExpedientesPorSistemaOrigenReparticion",
        "consultarIdFCPorNumeroExpediente",
        "validarExpediente"
        ],
    "consultaRegistro": [
        "consultarRegistroPorCUIT",
        "consultarRegistroPorNumero",
        "listarRegistroPublico",
        "listarTodosLosRegistrosPublicos"
        ],
    "consultarNumero": [
        "consultarNumero"
        ],
    "consultaTipoDocumento": [
        "consultarTipoDocumento"
        ],
    "consultaUsuario": [
        "buscarPorUsuario"
        ],
    "datosHistoricos": [
        "datosHistoricos"
        ],
    "documentosOficiales": [
        "desvincularDocumentosOficiales",
        "desvincularDocumentosOficialesConNumeroEspecial",
        "eliminarDocumentosOficialesNoDefinitivos",
        "hacerDefinitivosDocumentosOficiales",
        "vincularDocumentosOficiales",
        "vincularDocumentosOficialesConNumeroEspecial",
        "vincularDocumentosOficialesConTransaccionFC"
        ],
    "documentosTrabajo": [
        "adjuntarDocumentosTrabajo",
        "buscarArchivoTrabajo",
        "desadjuntarDocumentosTrabajo"
        ],
    "expedientesAsociados": [
        "asociarExpediente",
        "desasociarExpediente"
        ],
    "ffcc": [
        "buscarPorNombre"
        ],
    "generacionDocumentos": [
        "generarDocumento",
        "generarDocumentoUsuarioExterno"
        ],
    "generacionExpediente": [
        "generarCaratulaExpediente"
        ],
    "generacionPaseExpediente": [
        "generarPaseExpediente",
        "generarPaseExpedienteConBloqueo",
        "generarPaseExpedienteConDesbloqueo",
        "generarPaseExpedienteSinDocumento"
        ],
    "generarTareaGEDO": [
        "generarTareaGEDO"
        ],
    "tramitacionConjunta": [
        "desvincularTramitacionConjunta",
        "vincularTramitacionConjunta"
        ],
    "tratas": [
        "buscarTratasPorCodigo"
        ],
}

@app.get("/test_servicios", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "dic_metodos": dic_metodos,
        }
    )