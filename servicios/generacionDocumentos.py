from requests import post
from zeep import Settings, Client
import time
import xmltodict

class GeneracionDocumentos:
    
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

    def generarDocumento(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.generarDocumento(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s

    def generarDocumentoUsuarioExterno(self, request):
        token = self.obtenerToken()
        settings = Settings(extra_http_headers={'Authorization': 'Bearer ' + token}, raw_response=True)       
        cliente = Client(wsdl=self.url_servicio, settings=settings)
        t_ini = time.perf_counter()
        response = cliente.service.generarDocumentoUsuarioExterno(**request)
        t_fin = time.perf_counter()
        codigo = response.status_code
        respuesta = response.content.decode('utf-8')
        t_total = t_fin - t_ini
        t_total_s = str("%.2f" % t_total)
        return codigo,respuesta,t_total_s


if __name__ == '__main__':
    
    url_token = 'https://iop.hml.gba.gob.ar/servicios/JWT/1/REST/jwt'
    auth = ('ws_gdeba_hml_dpma_wstestgdeba', 'dpma*123',)
    url = 'https://iop.hml.gba.gob.ar/servicios/GDEBA/1/SOAP/generacionDocumentos?wsdl'


    request = {
        'request': {
            'acronimoTipoDocumento': 'TESTL',
            'data': bytes('Documento de prueba. Carece de motivación administrativa.','utf-8'),
            'usuario': 'USERT',
            'referencia': 'Documento de prueba. Carece de motivación administrativa.',
            'listaUsuariosDestinatariosExternos': {
                'entry': {
                    'key': '',
                    'value': ''
                }
            },
            'metaDatos': {
                'entry': {
                    'key': '',
                    'value': ''
                }                
            },
        }
    }
    

    servicio = GeneracionDocumentos(url, url_token, auth)
    cod,resp = servicio.generarDocumento(request)
    print('## generarDocumento ##')
    print(f'Codigo: {cod}')
    d = xmltodict.parse(resp)
    resp_numero = d['soap:Envelope']['soap:Body']['iop:generarDocumentoResponse']['return']['numero']
    print(resp_numero)