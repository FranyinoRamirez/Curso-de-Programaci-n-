nombre_usuario = "Franyino"  # Una variable 'nombre_usuario' que guarda el texto "Franyino"

edad = 21            # Una variable 'edad' que guarda el número 21 

fecha_de_nacimiento = 12_07_2004            # Una variable 'fecha_de_nacimiento' que guarda una fecha en formato numérico

es_estudiante = True   # Una variable 'es_estudiante' que guarda un valor booleano

print(nombre_usuario)  # Imprime: Franyino
print(edad)            # Imprime: 21

# Tradicional

print("El nombre del usuario es " + nombre_usuario)  # Concatena cadenas

# f-string

print(f"El nombre del usuario es {nombre_usuario} y tengo {edad} años y mi fecha de nacimiento es {fecha_de_nacimiento}")  # Usa f-string para formatear

name = input("¿Cuál es tu nombre? ")  # Solicita al usuario que ingrese su nombre
print(f"Hola, {name}!")  # Saluda al usuario por su nombre

edad_usuario = input("¿Cuántos años tienes? ")  # Solicita al usuario que ingrese su edad
print(f"Tienes {edad_usuario} años.")  # Informa al usuario de su edad

fecha_de_nacimiento_usuario = input("¿Cuál es tu fecha de nacimiento? ")  # Solicita al usuario que ingrese su fecha de nacimiento
print(f"Tu fecha de nacimiento es {fecha_de_nacimiento_usuario}.")  # Informa al usuario de su fecha de nacimiento

es_estudiante_usuario = input("¿Eres estudiante? (True/False) ")  # Solicita al usuario que indique si es estudiante
print(f"Es estudiante: {es_estudiante_usuario}.")  # Informa al usuario si es estudiante
