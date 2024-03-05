from requests import post
from zeep import Settings, Client
import time

class ConsultaExpediente:
    
    def __init__(self, url_servicio, url_token, auth):
        self.url_servicio = url_servicio
        self.url_token = url_token
        self.auth = auth

    def obtenerToken(self):
            response = post(self.url_token, auth=self.auth)
            status = response.status_code
            if status != 200:
                raise Exception(f'Error al obtener token ({status})')
            return response.content.decode('UTF-8')

    def consultarCaratulaVariablePorNumeroExpedienteUsuario(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.consultarCaratulaVariablePorNumeroExpedienteUsuario(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarCaratulaPorNumeroExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarCaratulaPorNumeroExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def consultarIdFCPorNumeroExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.consultarIdFCPorNumeroExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarHistorialPasesExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarHistorialPasesExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarExpedientesPorSistemaOrigenUsuario(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarExpedientesPorSistemaOrigenUsuario(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarExpedientePorIdSistemaExterno(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarExpedientePorIdSistemaExterno(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def consultarExpedienteDetallado(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.consultarExpedienteDetallado(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarCodigoCaratulaPorNumeroExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarCodigoCaratulaPorNumeroExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarDatosExpedienteVariable(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarDatosExpedienteVariable(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def validarExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.validarExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def consultarExpedientesPorSistemaOrigenReparticion(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.consultarExpedientesPorSistemaOrigenReparticion(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarDatosExpedientePorCodigosTrata(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarDatosExpedientePorCodigosTrata(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def buscarExpedientesPorSistemaOrigenLibreUsuario(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.buscarExpedientesPorSistemaOrigenLibreUsuario(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def consultarExpedientesPorSistemaOrigenLibreReparticion(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.consultarExpedientesPorSistemaOrigenLibreReparticion(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s