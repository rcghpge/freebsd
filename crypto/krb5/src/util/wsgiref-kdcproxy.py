import kdcproxy
import os
import ssl
import sys
from wsgiref.simple_server import make_server

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 8443
if len(sys.argv) > 2:
    pem = sys.argv[2]
else:
    pem = '*'

server = make_server('localhost', port, kdcproxy.Application())
sslctx = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
# Restrict to TLSv1.2 and higher
try:
    sslctx.minimum_version = ssl.TLSVersion.TLSv1_2
except AttributeError:
    # For Python versions < 3.7, set protocol options manually
    sslctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
sslctx.load_cert_chain(certfile=pem)
server.socket = sslctx.wrap_socket(server.socket, server_side=True)
os.write(sys.stdout.fileno(), b'proxy server ready\n')
server.serve_forever()
