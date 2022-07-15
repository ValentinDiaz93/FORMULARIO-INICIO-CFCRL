import cryptocode

str_encoded = cryptocode.encrypt("tcp:qa-centrolaboral-db.6ff6bdb9798a.database.windows.net,1433;DATABASE=CONTROL_DE_ASISTENCIA;UID=dtictiusr;PWD=P'T.j$4hdFU5X}u%m.gU","ENCRIPTADO")


str_decoded = cryptocode.decrypt(str_encoded, "ENCRIPTADO")
print("\n")
print("ESTE ES EL ORIGINAL: ",str_decoded)
print("\n")

print("ESTE ES EL ENCRIPTADO",str_encoded)

file = open("prueba.txt", "w")

# file.write("\n")
# print("ESTE ES EL ENCRIPTADO")
# print("\n")
# file.write(str_encoded)
# file.write("\n")
# print("ESTE ES EL DESENCRIPTADO")
# file.write(str_decoded)

#  https://www.delftstack.com/es/howto/python/python-encrypt-string/