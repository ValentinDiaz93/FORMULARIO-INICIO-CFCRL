## Declaración librería base64

import base64
from typing import TextIO

# # ---------------- INICIO  PRUEBAS DE   ENCRIPTADO Y FORMULARIO
# def encriptado():
#
#
#
# #------------------------------------  FIN PRUEBAS DE   ENCRIPTADO Y FORMULARIO



#ARCHIVO DE DONDE LEE LA INFORMACION SIN DESENCRIPTAR
with open('txt/sin_encriptar.txt', 'r') as f:  # r= read y es solo para leer el txt que se llama sin_encriptar
    contents = f.read()
    # IMPRIMIR CONTENIDO

    data = contents
    # Codificación Base 64 segura de URL y nombre de archivo
    urlSafeEncodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"))
    urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")

    #AQUI SE IMPRIME EL ENCRIPTADO EN LA TERMINAL DE PYCHARM
   # print(urlSafeEncodedStr + "\n")

#ESCRIBE EL TEXTO ENCRIPTADO

    f = open("txt/encriptado.txt", 'w')   # w= write y es solo para sobreescribir en el txt que se llama encriptado
    f.write(urlSafeEncodedStr)
    f.write("\n")
    f.close()


    


#    Desencriptar contenido almacenado en archivo de Texto
    print(contents)
    encodedStr = str(urlSafeEncodedBytes, "utf-8")
    # print ("Encriptado g: " , encodedStr)
    # Url Safe Base64 Desencriptado
    decodedBytes = base64.urlsafe_b64decode(encodedStr)
    decodedStr = str(decodedBytes, "utf-8")
    # print("Desencriptado: " , decodedStr)

#      Escribe la cadena de conexión al archivo de texto llamado conexcion_BD  (Decodificado)
f = open("txt/conexion_BD.txt", 'w')
f.write(contents)
f.close()