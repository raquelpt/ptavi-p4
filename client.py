#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
import ast


numparametros = len(sys.argv)

# Cliente UDP simple.

# Dirección IP del servidor.
server = sys.argv[1]
port = ast.literal_eval(sys.argv[2])

# Contenido que vamos a enviar
line = str()
for i in range(3, numparametros):
    line = line+" "+str(sys.argv[i])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((server, port))

print "Enviando: " + line
my_socket.send(line + '\r\n')
data = my_socket.recv(1024)

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
