import os
import ssl
from wsgiref.simple_server import make_server, WSGIRequestHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
from django.core.wsgi import get_wsgi_application


django.setup()
application = get_wsgi_application()

HOST = '0.0.0.0'
PORT = 8000
CERT_FILE = os.path.join(os.path.dirname(__file__), 'certs', 'localhost.crt')
KEY_FILE = os.path.join(os.path.dirname(__file__), 'certs', 'localhost.key')

httpd = make_server(HOST, PORT, application, handler_class=WSGIRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f'Serving HTTPS on https://localhost:{PORT}/')
httpd.serve_forever()
