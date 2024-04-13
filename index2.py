# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")

# Saludar al usuario utilizando su nombre
if nombre.strip() == "":
    print("No ingresaste un nombre válido.") #true
else:
    print("Hola, {}! Bienvenido al mundo de Python.".format(nombre)) #false
