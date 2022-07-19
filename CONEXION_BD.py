#---------------IMPORTA LIBRERIAS
import base64

from typing import TextIO

# # ---------------------------------------------------  ABRE EL ARCHIVO CON EL TEXTO SIN ENCRIPTAR Y LO LEE
with open('ENCRIPT/sin_encriptar.txt', 'r') as f:  # r= read y es solo para leer el txt que se llama sin_encriptar
    contents = f.read()
    # IMPRIMIR CONTENIDO

    data = contents
    # Codificación Base 64 segura de URL y nombre de archivo
    urlSafeEncodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")

    # AQUI SE IMPRIME EL ENCRIPTADO EN LA TERMINAL DE PYCHARM
    # print(urlSafeEncodedStr + "\n")

    #                          ESCRIBE EL TEXTO ENCRIPTADO   EN EL TXT
    f = open("ENCRIPT/encriptado.txt", 'w')  # w= write y es solo para sobreescribir en el txt que se llama encriptado
    f.write(urlSafeEncodedStr)
    f.write("\n")
    f.close()

    #     Desencriptar contenido almacenado en archivo de Texto
    print(contents)
    # encodedStr = Str
    print ("Encoded String: " , encodedStr)
    # Url Safe Base64 Decoding
    decodedBytes = base64.urlsafe_b64decode(encodedStr)
    decodedStr = str(decodedBytes, "utf-8")
    print("Decoded String: " , decodedStr)

#      Escribe la cadena de conexión al archivo de texto llamado works2.txt  (Decodificado)
f = open("conexion_BD.txt", 'W')
f.write(contents)
f.close()