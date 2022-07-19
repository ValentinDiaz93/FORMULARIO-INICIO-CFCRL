
#CONEXION A BASE DE DATOS POSTGRES
# conn = psycopg2.connect(host='localhost',database='postgres',user='postgres',password='1802Diaz')


#Recorte de Cadena de Texto

#postgres://usuarioMTY:0180Diaz2@172.16.63.150:5432/postgres

str1 = "postgres,usuarioMTY,0180Diaz2,172.16.63.150,5432,postgres"  #CADENA DE CONEXION A POSTGRES
lista1 =  str1.split (',')    #SEPARA POR COMAS
print (lista1)  # IMPRIME LA LISTA PERO CON LAS COMAS




 
 
# IMPRIMIR LISTA ORIGINAL
print ("LISTA ORIGINAL ES  : " + str(lista1))   #IMPRIME LISTA  ORIGINAL
 
# VARIABLES
var1, var2, var3, var4, var5 = [lista1[i] for i in (1, 2, 3, 4, 5 )]

# printing result
print ("LAS VARIABLES SON :   " + str(var1)  +
                            " " + str(var2) +
                            " " + str(var3) +
                            " " + str(var4) +
                            " " + str(var5) )