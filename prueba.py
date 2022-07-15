## Declaración librería base64
# !/usr/bin/python3
import base64

# Leer el archivo
# !/usr/bin/env python
# read_width.py
from typing import TextIO

#ARCHIVO DE DONDE LEE LA INFORMACION SIN DESENCRIPTAR
with open('ENCRIPT/sin_encriptar.txt', 'r') as f:  # r= read y es solo para leer el txt que se llama sin_encriptar
    contents = f.read()
    # IMPRIMIR CONTENIDO

    data = contents
    # Codificación Base64 segura de URL y nombre de archivo
    urlSafeEncodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
    print(urlSafeEncodedStr + "\n")

    f = open("ENCRIPT/encriptado.txt", 'w')   # w= write y es solo para sobreescribir en el txt que se llama encriptado
    f.write(urlSafeEncodedStr)
    f.write("\n")
    f.close()

    ##     Desencriptar contenido almacenado en archivo de Texto
    # IMPRIMIR CONTENIDO
    #encodedStr = Str
    #print ("Encoded String: " , encodedStr)
    # Url Safe Base64 Decoding
    #decodedBytes = base64.urlsafe_b64decode(encodedStr)
    #decodedStr = str(decodedBytes, "utf-8")
    #print("Decoded String: " , decodedStr)

##      Escribe la cadena de conexión al archivo de texto llamado works2.txt  (Decodificado)
#f = open("works2.txt", 'a')
#f.write(contents)
#f.close()