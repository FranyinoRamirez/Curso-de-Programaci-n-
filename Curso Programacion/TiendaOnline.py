import time
compras = []
precios = []

print("""✨ ¡Hola! Qué alegría verte por aquí ✨
Bienvenido a Tu tiendaOnline. Hemos seleccionado cada producto pensando en ti, 
para que encuentres exactamente lo que buscas con la mejor calidad. 🛒""")
time.sleep(2)
while True:
    while True:
        print("=========================")
        print("[2] Ir a caja (Pagar)")
        print("=========================")
        print("[3] Borrar último (Producto)")
        print("=========================")
        producto = input("Ingresa un producto: ").lower()
        
        if producto == "2":
            break 
        
        elif producto == "3":
            if len(compras) > 0:
                compras.pop()
                precios.pop()
                print("===== Último eliminado =====")
            else:
                print("===== Carrito vacío =====")
        else:
            print("=========================")
            precio = float(input(f"Precio de {producto}: $"))
            compras.append(producto)
            precios.append(precio)

    print("========== REVISIÓN DE TU CARRITO ==========")
    for i in range(len(compras)):
        print(f"- {compras[i]}: ${precios[i]}")
    print("========== REVISIÓN DE TU CARRITO ==========")   
    confirmar = input("¿Todo listo? Escribe 'si' para pagar o 'no' para seguir comprando: ").lower()
    
    if confirmar == "si":
        break
    else:
        print("¡Volvamos a la tienda!")
       
total = sum(precios)
print("========== TICKET FINAL ==========")
for i in range(len(compras)):
    print(f"{compras[i]} .... ${precios[i]}")
print("========== TICKET FINAL ==========") 

print(f"TOTAL PAGADO: ${total}")
print("¡Gracias por su compra!")