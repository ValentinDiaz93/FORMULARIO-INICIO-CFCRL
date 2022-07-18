# CONEXION A BASE DE DATOS POSTGRES
# LA CADENA DE CONEXION ES:
# conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='1802Diaz')

import base64

# ******** LEE EL ARCHIVO TXT SIN ENCRIPTAR (los datos ingresados por el formulario)*******
with open('ENCRIPT/sin_encriptar.txt', 'r') as f:  # r= read y es solo para leer el txt que se llama sin_encriptar
    str1 = f.read()
    conn = str1.split(',')  # SEPARA POR COMAS
    # lista1 = str1.split(',')  # SEPARA POR COMAS
    print(conn)  # IMPRIME LA LISTA PERO CON LAS COMAS

# ********** Hasta aqui me lee el txt sin encriptar y me separa por comas **************



