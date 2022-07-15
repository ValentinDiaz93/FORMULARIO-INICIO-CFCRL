# FORMULARIO PARA CONEXION

# Importo la libreria tkinter, con esta puedo crear mi interfaz gráfica

from tkinter import *


# -------------------------------------Manipular datos de campos de registro-----------------------------
def enviar_datos():
    # Recuperar datos
    username_info = username.get()
    password_info = password.get()
    host_info = host.get()
    base_info = str(base.get())
    # Imprimir los datos
    print(username_info, "\t", password_info, "\t", host_info, "\t", base_info)
# --------------------------------------------------------------------------------------------------------

# -------------------------- Abrir y escribir datos en un archivo-----------------------------------------
# open- Crea un archivo de texto y escribe en el
# a= append (agrega la informacion al final de lo que ya se tenia en el archivo

#Si quiero que se almacenen todos los datos en el txt solo cambio la "w" por "a"


# w= write (Escribe en un archivo)
# El nombre del archivo a crear sera  registros

    file = open("ENCRIPT/sin_encriptar.txt", "w")
    file.write(username_info)
    #Se agrega la tabulacion (\t) para darle formato
    file.write("\n")
    file.write(password_info)
    #Se agrega la tabulacion (\t) para darle formato
    file.write("\n")
    file.write(host_info)
    #Se agrega la tabulacion (\t) para darle formato
    file.write("\n")
    file.write(base_info)
    #Se agrega la tabulacion (\t) para darle formato
    file.write("\n")
    file.close()
    print(" New user registered. Username: {} | host: {}   ".format(username_info, host_info))

# ------------------------------ ELIMINAR LOS DATOS QUE SE INGRESARON ANTERIORMENTE -------------------------
    #el metodo delete borrara todos lo que exista
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    host_entry.delete(0, END)
    base_entry.delete(0, END)

# ------------------------------VENTANA Y SUS CARACTERISTICAS----------------------------------------
# CREAR INSTANCIA DE LA CLASE TK
ventana = Tk()
# TAMAÑO DE LA VENTANA
ventana.geometry("650x501")
# TITULO DE LA VENTANA
ventana.title("Inicio de sesión al control de Asistencia del CFCRL")
# Accion que evita que se cambie de tamaño la ventana
ventana.resizable(False, False)
# Color de fondo de la ventana (USE EL CAFE INSTITUCIONAL)
ventana.config(background="#B38E5D")









# --------------------------------------------------------------------------------------------------------


# --------------------------TITULO PRINCIPAL DEL MENU (main_title)----------------------------------------
# text es el texto a  mostrar
# font Es el tipo de fuente
# bg es el color de background (fondo)  use el rojo institucional
# fg es el color del texto
# width es el ancho en caracteres
# height es la altura
main_title = Label(text="INICIO DE SESIÓN  CONTROL DE ASISTENCIA CFCRL ", font=("Consolas bold", 16),
                   bg="#9D2449", fg="#FFFAF0", width="500", height="2")
# --------------------------------------------------------------------------------------------------------

main_title.pack()

# -----------------------CAMPOS DE TEXTO EN EL FORMULARIO-------------------------------------------------
# label es el campo de texto para cada campo del formulario
# place es para posicionar el texto dentro de la ventana
# bg es el color de background (fondo)
# fg es el color del texto
# x es la posicion de la etiqueta en el eje x
# y es la posicion de la etiqueta en el eje y
username_label = Label(text="USERNAME", font=("Consolas bold", 12), bg="#9D2449",fg="#FFFFFF")
username_label.place(x=20, y=75)
password_label = Label(text="PASSWORD", font=("Consolas bold", 12), bg="#9D2449",fg="#FFFFFF")
password_label.place(x=20, y=135)
host_label = Label(text="HOST", font=("Consolas bold", 12), bg="#9D2449",fg="#FFFFFF")
host_label.place(x=20, y=195)
base_label = Label(text="DATABASE", font=("Consolas bold", 12), bg="#9D2449",fg="#FFFFFF")
base_label.place(x=20, y=255)

# --------------------------------------------------------------------------------------------------------

#  -------------------------AQUI SE OBTIENEN Y ALMACENAN LOS DATOS----------------------------------------
# NOMBRE DE LAS VARIABLES Y EL TIPO DE DATO QUE MANEJAN
username = StringVar()
password = StringVar()
host = StringVar()
base = StringVar()

# text variable asocia la entrada con el campo de entrada de los datos
# width es el largo del espacio donde capturamos los valores
username_entry = Entry(textvariable=username, width="70")
# show nos mostrara un * en lugar de lo que se ha tecleado por el usuario
password_entry = Entry(textvariable=password, width="70", show="*")
host_entry = Entry(textvariable=host, width="70")
base_entry = Entry(textvariable=base, width="70")

#place se ocupa para la posicion de los campos de la entrada de datos
# x es la posicion del campo de entrada de datos en el eje x
# y es la posicion del campo de entrada de datos en el eje y
username_entry.place(x=20, y=105)
password_entry.place(x=20, y=165)
host_entry.place(x=20, y=225)
base_entry.place(x=20, y=285)

# --------------------------------------------------------------------------------------------------------

# ---------------------BOTON QUE AL HACER CLIC NOS ALMACENA LOS DATOS-------------------------------------
# command nos lleva a una parte del código donde captura y manipulan los datos ingresados por el usuario
iniciar_btn = Button(ventana, text="INICIAR SESIÓN", width="30", height="2", command=enviar_datos,
                     font=("Consolas bold", 13),fg="#FFFFFF", bg="#2C572C")
iniciar_btn.place(x=22, y=320)

ventana.mainloop()
