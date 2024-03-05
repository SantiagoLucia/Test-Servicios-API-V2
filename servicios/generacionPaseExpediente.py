from requests import post
from zeep import Settings, Client
import time

class GeneracionPaseExpediente:
    
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

    def generarPaseExpedienteSinDocumento(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)        
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.generarPaseExpedienteSinDocumento(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def generarPaseExpedienteConDesbloqueo(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.generarPaseExpedienteConDesbloqueo(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def generarPaseExpedienteConBloqueo(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.generarPaseExpedienteConBloqueo(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def generarPaseExpediente(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.generarPaseExpediente(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s