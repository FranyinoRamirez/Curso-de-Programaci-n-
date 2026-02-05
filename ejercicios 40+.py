#1. Promedios Inteligentes: Crea una función que reciba una lista de notas. Usa un bucle para sumarlas y un condicional para imprimir "Aprobado" (si es >60) o "Reprobado".

def promedios_inteligentes():
    notas = []
    print("--- Registro de Notas ---")
    print("Escribe una nota y pulsa Enter. (Escribe 'fin' para terminar)")

    while True:
        entrada = input("Ingresa una nota: ")
        
        if entrada.lower() == "fin":
            break
        nota = float(entrada)
        notas.append(nota)

    if len(notas) > 0:
        suma_total = 0
        
        for n in notas:
            suma_total += n
            
        promedio = suma_total / len(notas)
        
        print(f"\nTu promedio final es: {promedio:.2f}")
        
        if promedio > 60:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Reprobado")
    else:
        print("No se ingresaron notas para calcular.")

promedios_inteligentes()

#-------------------------------------------------------------------------------------------------------------------------------------------
#2. Filtro de Rangos: Genera un bucle que recorra del 1 al 100. Crea una función que determine si el número es par Y múltiplo de 3 a la vez.

def es_par_y_multiplo_de_3(numero):
    if numero % 2 == 0 and numero % 3 == 0:
        return True
    else:
        return False
print("Números que cumplen ambas condiciones:")

for i in range(1, 101):
    if es_par_y_multiplo_de_3(i):
        print(f"El {i} es par y múltiplo de 3")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#3. Login Seguro: Diseña un sistema con while que pida contraseña. Tienes solo 3 intentos (usa un contador). Si acierta, usa break y saluda al usuario.

def sistema_login():
    clave = "1234q4"
    intentos = 3

    print("===Sitestema de Seguridad===")

    while intentos > 0:
        contraseña = input(f"Introdiice la Contraseña")
        if contraseña == clave:
            print("Acceso concedido")
            break
        else:
            intentos -= 1 
            if intentos > 0:
             print("Contraseña Incorrecta")
            else:
                print("Acceso Bloqueado")
sistema_login()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4. Conversor Selectivo: Toma una lista de distancias en KM. Crea una función que las pase a Millas, pero solo si la distancia es mayor a 0 (ignora errores con if).

def conversor_interactivo():
    distancias_millas = []
    factor_conversion = 0.621369647819236

    entrada_cantidad = input("Cuántas distancias vas a ingresar?: ")
    cantidad = int(entrada_cantidad)
    
    for i in range(cantidad):
        valor = float(input(f"Ingresa la distancia #{i+1} en KM: "))
        
        if valor > 0:
            millas = valor * factor_conversion
            distancias_millas.append(round(millas, 2))
        else:
            print(f"X El valor {valor} es inválido y será ignorado.")

    print("===Resultado de la Conversión===")
    print(f"Lista final en millas: {distancias_millas}")

conversor_interactivo()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#5. Buscador de Letras: Pide una frase y una letra. Tu función debe recorrer el texto y decir cuántas veces aparece, pero si no aparece ninguna, debe avisar con un error.

def buscador_de_letras():
    frase = input("Ingresa una frase: ")
    letra_objetivo = input("Qué letra quieres buscar?: ")

    contador = 0

    for letra in frase:
        if letra.lower() == letra_objetivo.lower():
            contador += 1
    if contador > 0:
        print(f"¡Exito! La letra '{letra_objetivo}' aparece {contador} veces.")
    else:
        print(f"Error: La letra '{letra_objetivo}' no se encuentra en la frase.")
buscador_de_letras()

#6. Salto de Números: Imprime los números del 1 al 20, pero tu función debe usar continue para saltarse todos los múltiplos de 4.

def saltar_multiplos():
    print("Contando del 1 al 20 (saltando multiplos de 4):")
    
    for numero in range(1, 21):
        if numero % 4 == 0:
            continue
            
        print(numero, end=" ")

saltar_multiplos()

#7. Control de Stock: Tienes un diccionario con productos y cantidades. Crea una función que reciba una "orden de compra" (lista) y descuente el stock solo si hay disponibilidad.

def procesar_pedido(inventario, orden_compra):
    print("--- Procesando Pedido ---")
    
    for producto in orden_compra:
        if producto in inventario:
            if inventario[producto] > 0:
                inventario[producto] -= 1
                print(f"{producto.capitalize()}: Despachado. (Quedan {inventario[producto]})")
            else:
                print(f"{producto.capitalize()}: Agotado.")
        else:
            print(f"{producto.capitalize()}: No forma parte de nuestro catálogo.")
            
    return inventario

stock_actual = {
    "Cpu": 5,
    "Gpu": 2,
    "Ram": 0,
    "Monitor": 3
}

pedido_cliente = ["Cpu", "Gpu", "Ram", "Monitor"]

stock_final = procesar_pedido(stock_actual, pedido_cliente)

print("\nStock actualizado:", stock_final)

#--------------------------------------------------------------------------------------------------------------------------------------------------

#8. Números Primos: Crea una función que reciba un límite. Usa bucles anidados para encontrar todos los primos hasta ese número. ¡Cuidado con la lógica!

def encontrar_primos(limite):
    primos = []

    for num in range(2, limite + 1):
        es_primo = True
        
        for i in range(2, num):
            if num % i == 0:
                es_primo = False 
                break 
        
        if es_primo:
            primos.append(num)
            
    return primos

limite_usuario = int(input("Hasta que numero quieres buscar primos?: "))
resultado = encontrar_primos(limite_usuario)

print(f"Los números primos hasta el {limite_usuario} son:")
print(resultado)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#9. Calculadora de IVA: Recorre una lista de precios. Si el producto cuesta más de $100, aplica un IVA del 16% dentro de la función; si cuesta menos, aplica solo el 8%.

def calculadora_iva_pro():
    precios_con_iva = []
    
    print("====Sistema de Facturación Interactiva====")
    print("Ingresa los precios." "Escribe 0 Finalizar.")
    
    while True:
        try:
            precio_base = float(input("Precio del producto: $"))
            
            if precio_base <= 0:
                break
            
            if precio_base > 100:
                iva = 0.16
                tipo_iva = "16% (Tasa General)"
            else:
                iva = 0.08
                tipo_iva = "8% (Tasa Reducida)"
            
            monto_iva = precio_base * iva
            total = precio_base + monto_iva
            
            precios_con_iva.append(round(total, 2))
            
            print(f">> Impuesto aplicado: {tipo_iva}")
            print(f">> Monto IVA: ${monto_iva:.2f}")
            print(f">> Total a pagar: ${total:.2f}")
            
        except ValueError:
            print("Error: Por favor ingresa un número válido (usa punto para decimales).")

    if precios_con_iva:
        print("" + "="*30)
        print(f"RESUMEN DE FACTURA:")
        print(f"Total productos: {len(precios_con_iva)}")
        print(f"Lista de totales: {precios_con_iva}")
        print(f"Gran total acumulado: ${sum(precios_con_iva):.2f}")
        print("="*30)
    else:
        print("No se procesaron productos.")

calculadora_iva_pro()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#10. Menú de Cajero: Usa un while True para mostrar un menú: 1. Ver saldo, 2. Retirar, 3. Salir. Valida con if que el retiro no supere el saldo disponible.

saldo = 100

while True:
    print("\n--- MENU DE CAJERO ---")
    print("1. Ver saldo")
    print("2. Retirar")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        
    
        if monto > saldo:
            print("Error: Fondos insuficientes.")
        elif monto <= 0:
            print("Error: Ingrese un monto valido mayor a cero.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
    
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break 
    
    else:
        print("Opción no valida. Intente de nuevo.")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#11. Limpiador de Nombres: Dada una lista de usuarios con espacios y símbolos, usa un bucle para limpiar los textos y una función para validar que el nombre sea real.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#12. Espejo de Palabras: Crea una función que reciba una lista de palabras y devuelva solo las que sean palíndromos (se leen igual al revés) y tengan más de 5 letras.
def filtrar_palindromos_largos(lista_palabras):
    palindromos_seleccionados = []
    
    for palabra in lista_palabras:
        palabra = palabra.strip().lower()
        
        palabra_invertida = palabra[::-1]
        
        if palabra == palabra_invertida and len(palabra) > 5:
            palindromos_seleccionados.append(palabra)
            
    return palindromos_seleccionados

palabras_prueba = ["reconocer", "radar", "sometemos", "oro", "luz", "anilina", "python"]

resultado = filtrar_palindromos_largos(palabras_prueba)

print("Palabras que son palindromos y tienen mas de 5 letras:")
print(resultado)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#13. Factorial Validado: Pide un número. Usa while para asegurar que sea positivo y un for para calcular el factorial mediante una función acumuladora.

def calcular_factorial():
    while True:
        entrada = input("Ingresa un numero entero positivo para calcular su factorial: ")
        
        if entrada.isdigit():
            numero = int(entrada)
            if numero >= 0:
                break
            else:
                print("Error: El numero debe ser mayor o igual a cero.")
        else:
            print("Error: Por favor, ingresa solo numeros enteros.")

    resultado = 1
    
    if numero == 0:
        resultado = 1
    else:
        for i in range(1, numero + 1):
            resultado *= i  
    print(f"El factorial de {numero} es: {resultado}")

calcular_factorial()

#--------------------------------------------------------------------------------------------------------------------------------------------------------