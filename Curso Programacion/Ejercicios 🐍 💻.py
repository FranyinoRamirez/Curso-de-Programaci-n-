#1. Calculadora de Área de Rectángulo 📐
"""Enunciado: Calcula el área de un rectángulo pidiendo base y altura.
- Requerimientos: Pedir datos, convertir a número, calcular y mostrar """

base = int(input("Introduce la base del rectángulo: "))

altura = int(input("Introduce la altura del rectángulo: "))

area = base * altura
print(f"El área del rectángulo es: {area}")


#2. Conversor de Temperatura 🌡️
"""- Enunciado: Convierte grados Celsius a Fahrenheit.
- Requerimientos: Pedir Celsius, 
aplicar la fórmula   F = (C * 9/5) + 32 y mostrar."""

C = int(input("Introduce la temperatura en grados Celsius: "))
F = (C * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {F}")


#3. Concatenación de Cadenas ✍️
"""- Enunciado: Pide nombre y apellido y muéstralos juntos.
- Requerimientos: Usar input() y el operador + para unir los strings con un espacio."""

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
print(f"Tu nombre completo es: {nombre} {apellido}")


#4. Verificador de Número Par o Impar 🔢
"""- Enunciado: Determina si un número es par o impar.
- Requerimientos: Usar el operador módulo (%) y un if-else."""

num = int(input("Numero: "))
if num % 2 == 0:
    print(f"El número {num} es par.")   
else:
    print(f"El número {num} es impar.")


#5. Elegibilidad para Votar 🗳️
"""- Enunciado: Verifica si alguien puede votar por su edad.
- Requerimientos: Pedir edad y usar un if para ver si es >= 18."""

edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres elegible para votar.")  
else:
    print("No eres elegible para votar.")


#6. Comparador de Números ⚖️
"""- Enunciado: Compara dos números (mayor, menor o igual).
- Requerimientos: Usar una estructura if-elif-else."""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
else:
    print(f"{num1} es igual a {num2}")


    #7. Operadores Lógicos 🧠
    """- Enunciado: Determina si un número está entre 10 y 20.
- Requerimientos: Usar el operador and en la condición."""

num = int(input("Introduce un número: "))
if num >= 10 and num <= 20: 
    print(f"El número {num} está entre 10 y 20.")
else:
    print(f"El número {num} no está entre 10 y 20.")

#8. Verificación de Contraseña Simple 🔐
"""- Enunciado: Simula un login simple.
- Requerimientos: Guardar una contraseña en una variable, pedirla al usuario y comparar."""


contraseña = "123456"
contraseña_usuario = input("Introduce la contraseña: ")

if contraseña == contraseña_usuario:
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")



#9. Calculadora de Descuento 💰
"""- Enunciado: Calcula un descuento del 15% si el precio supera los $100.
- Requerimientos: Usar if-else para aplicar el descuento y mostrar el precio final."""


precio = float(input("Introduce el precio del producto: $"))   
if precio > 100:
    descuento = precio * 0.15
    precio_final = precio - descuento
    print(f"El precio final con descuento es: ${precio_final:.2f}")
else:
    print(f"El precio final es: ${precio:.2f}")

    #10. Clasificador de Números ➕➖
    """Enunciado: Indica si un número es positivo, negativo o cero.
- Requerimientos: Implementar con una cadena if-elif-else."""

num = int(input("Introduce un número: "))
if num > 0:
    print(f"El número {num} es positivo.")
elif num < 0:
    print(f"El número {num} es negativo.")
else:
    print(f"El número {num} es cero.")


#Año Bisiesto 🗓️
""" - Enunciado: Determina si un año es bisiesto.
- Requerimientos: Usar condicionales anidados o lógicos para la regla completa."""

año = int(input("Introduce un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")     
else:
    print(f"El año {año} no es bisiesto.")

#12. Calculadora de Calificaciones 🎓
"""- Enunciado: Convierte una nota de 0-100 a A, B, C, D, F.
- Requerimientos: Usar if-elif-else para los rangos de notas."""

nota = int(input("Introduce la nota (0-100): "))
if nota >= 90:  
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")  
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")
    
#13. Verificador de Vocal o Consonante 🅰️
"""- Enunciado: Pide un carácter y di si es vocal o consonante.
- Requerimientos: Convertir a minúscula y usar or o in para chequear."""

caracter = input("Introduce un carácter: ").lower()
if caracter in 'aeiou':
    print(f"El carácter '{caracter}' es una vocal.")        
else:
    print(f"El carácter '{caracter}' es una consonante.")

#14. Selección de Menú 📋
"""- Enunciado: Simula un menú con 3 opciones y una respuesta para cada una.
- Requerimientos: Usar if-elif-else para gestionar la elección del usuario."""

print("Menú:")
print("1. Opción 1")        
print("2. Opción 2")
print("3. Opción 3")

opcion = int(input("Elige una opción (1-3): "))
if opcion == 1:
    print("Has elegido la opción 1.")
elif opcion == 2:
    print("Has elegido la opción 2.")
elif opcion == 3:
    print("Has elegido la opción 3.")
else:
    print("Opción no válida.")

#15. Tipo de Triángulo 🔺
"""- Enunciado: Pide 3 lados e indica si el triángulo es equilátero, isósceles o escaleno.
- Requerimientos: Comparar los lados usando if-elif-else."""

lado1 = float(input("Introduce el primer lado del triángulo: "))
lado2 = float(input("Introduce el segundo lado del triángulo: "))
lado3 = float(input("Introduce el tercer lado del triángulo: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")


#16. El Mayor de Tres Números 🥇
"""- Enunciado: Encuentra el número más grande de tres ingresados.
- Requerimientos: ¡Prohibido usar la función max()! Resuélvelo con condicionales."""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número más grande es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número más grande es: {num2}")
else:
    print(f"El número más grande es: {num3}")


#17. Calculadora de IMC 💪
"""- Enunciado: Calcula el Índice de Masa Corporal y clasifícalo.
- Requerimientos: Pide peso y altura, calcula el IMC y usa if-elif-else para las categorías (Bajo peso, Normal, etc.)."""

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Categoría: Bajo peso")
elif 18.5 <= imc < 25:
    print("Categoría: Normal")
elif 25 <= imc < 30:
    print("Categoría: Sobrepeso")
else:
    print("Categoría: Obesidad")



#18. Calculadora de Costo de Envío 📦
"""- Enunciado: Calcula el costo de envío por peso y zona de destino, aplicando descuentos.
- Requerimientos: Usar condicionales anidados (zona y luego peso)."""

peso = float(input("Introduce el peso del paquete en kg: "))
zona = input("Introduce la zona de destino (local, nacional, internacional): ").lower()
if zona == "local":
    if peso <= 5:
        costo = 5.00
    else:
        costo = 10.00
elif zona == "nacional":
    if peso <= 5:
        costo = 10.00
    else:
        costo = 20.00
elif zona == "internacional":
    if peso <= 5:
        costo = 20.00
    else:
        costo = 40.00
else:
    costo = 0
    print("Zona no válida.")
if costo > 0:
    print(f"El costo de envío es: ${costo:.2f}")

#19. Resolución de Ecuación Cuadrática 🔬
"""- Enunciado: Resuelve una ecuación de segundo grado $ax^2 + bx + c = 0$.
- Requerimientos: Calcular el discriminante y usar if-elif-else para ver si hay 0, 1 o 2 soluciones reales."""

import math
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))    
c = float(input("Introduce el coeficiente c: "))
discriminante = b**2 - 4*a*c
if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Dos soluciones reales: {raiz1} y {raiz2}")
elif discriminante == 0:
    raiz = -b / (2*a)
    print(f"Una solución real: {raiz}")
else:
    print("No hay soluciones reales.")

#20. Juego: Piedra, Papel o Tijera 🗿📄✂️
"""- Enunciado: Implementa la lógica de un turno del juego.
- Requerimientos: Pedir jugadas a dos jugadores y usar condicionales anidados para encontrar al ganador o declarar empate."""

jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
if jugador1 == jugador2:
    print("Empate.")    
elif jugador1 == "piedra":
    if jugador2 == "tijera":
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")
elif jugador1 == "papel":
    if jugador2 == "piedra":
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")
elif jugador1 == "tijera":
    if jugador2 == "papel":
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")
else:
    print("Jugada no válida.")



#Fin del archivo Ejercicios🐍💻.py