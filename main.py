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

@app.get("/test_servicios", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
        }
    )