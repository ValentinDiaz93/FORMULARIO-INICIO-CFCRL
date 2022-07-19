## Declaración librería base64
# !/usr/bin/python3
import base64

## Leer el archivo
# !/usr/bin/env python
# read_width.py
from typing import TextIO

with open('ENCRIPT/sin_encriptar.txt', 'r') as f:
    contents = f.read()
    # print(contents)

    data = contents
    # URL and Filename Safe Base64 Encoding
    urlSafeEncodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
    print(urlSafeEncodedStr + "\n")


    f = open("ENCRIPT/encriptado.txt", 'w')   # w= write y es solo para sobreescribir en el txt que se llama encriptado
    f.write(urlSafeEncodedStr)
    f.write("\n")
    f.close()
    #     Desencriptar contenido almacenado en archivo de Texto
    print(contents)
    encodedStr = Str
    print ("Encoded String: " , encodedStr)
    # Url Safe Base64 Decoding
    decodedBytes = base64.urlsafe_b64decode(encodedStr)
    decodedStr = str(decodedBytes, "utf-8")
    print("Decoded String: " , decodedStr)

#      Escribe la cadena de conexión al archivo de texto llamado works2.txt  (Decodificado)
f = open("conexion_BD", 'w')   # w= write y es solo para sobreescribir en el txt que se llama encriptado
f.write(contents)
f.close()