import time  #Hace que algunos comandos demoren! time.sleep()
while True: #Un bocle para que el juego se repita siempre, así tengas un final bueno o malo.
    print("""¡Damos inicio a la MiniAventura🌍 ⛏️ 💎!
Prepárate para explorar, construir y sobrevivir en un mundo lleno de posibilidades.""")
    nombre = input("Introduce tu nombre: ")    #Aqui preguntamos el nombre para que sea mas como un juego "NickName"
    print(f"Tu nombre es: {nombre}")
    print("❤️ Vida: 20/20 | 🍖 Hambre: 20/20 | 🎒 Inventario: [Mapa 🗺️, Pan 🥖x3]")
    print("generando mundo MiniAventura🌍...".upper())
    time.sleep(2)                                   
    print("generando mundo MiniAventura🌍...".upper())
    time.sleep(3)
    print("""generando mundo MiniAventura🌍....
            [N]
    🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊
    🌊🚢🌊🌿🌿🌿🌿🏜️🏜️ 🌊
    🌊🌊🌿🌿🌳🌿🌿🏜️🏜️ 🌊
    🌊🌿🌿🌿🌿🌿🌿🏜️🏜️ 🌊
[O] 🌊🌿🌿🌿🏠🌿🌿🌿🌿🌊  [E]
    🌊🌿🌻🌿🌿🌿🌿🌿🌿🌊
    🌊🌿🌿🌿🌿🌿⛰️⛰️ 🌿🌊
    🌊🌿💜🌿🌿⛰️⛰️⛰️ 🌿🌊
    🌊🌊🌿🌿🌿🌿🌿🌿🌊🌊
    🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊
            [S]   
 Puntos de Aparición :
🌊 : (Oceano/Mar)x
🏜️  : (Tierras Desiertas)x
🌳 : (Bosque)x
🌻 : (Jardín Floral)       
🏠 : (Aldea)x
⛰️  : (Montaña/Cuevas)x    """.upper() )
    opcion = int(input("Elige una opción (1-6): ")) #La elección de mapa, también llamado 'bioma', es totalmente aleatoria para hacer el juego un poco más divertido. ¡JAJAJA!"

    if opcion == 1:
        print("""
Has elegido la opción 1. Punto de Aparición (Aldea🏠)
Apareces en medio de una aldea tranquila 🏘️. 
El viento sopla suavemente y escuchas el sonido de las campanas a lo lejos 🔔.
Al revisar tus bolsillos 🎒, notas que no vas con las manos vacías:
🗺️  1 Mapa en blanco (esperando ser dibujado).
🥖 3 Panes crujientes (recién horneados).
El sol brilla en lo alto ☀️, los aldeanos murmuran sus tratos 👨‍🌾 y el vasto
mundo de MiniAventure 🌍 se extiende ante ti.
    """)
        print("(Explorar la aldea) o (te Preparas para una aventura)")
        time.sleep(2)    
        decision1 = input("¿Qué deseas hacer? (explorar / preparar): ").lower()
        
        if decision1 == "explorar":
            print("""
¡Excelente trabajo! 🌟 Has demostrado una gran curiosidad al continuar con la exploración de la aldea 🏘️. 
Mientras recorrías los alrededores, uno de los aldeanos se ha fijado en tus habilidades y tiene un trato 
especial preparado para ti 🤝📜. ¡Parece una oportunidad que no deberías dejar pasar! 💎✨
    """)
            accion = input("¿Quieres CAMBIAR tus 3 panes por la casa o seguir EXPLORANDO?: ").lower()
            if accion == "cambiar":
                print("¡Increíble! Aceptaste el trato y, al entrar en tu nueva propiedad, ¡encontraste oro bajo el suelo! 🏠✨ Te has convertido en el héroe local y ahora vives con lujos en la aldea. 💰🏆")
            elif accion == "explorando":
                print("Decidiste no arriesgarte con el trato, pero la suerte no estuvo de tu lado 🌑. Te perdiste en la noche y un Creeper te alcanzó. 💥💀 Tu aventura termina aquí entre cenizas y pólvora.")
            else:
                print("💀 Has muerto por no tomar una decisión clara en la aldea.")
        elif decision1 == "preparar":
            print("💀 Mala decisión! Al elegir salir a la aventura sin estar listo, te quedaste sin comida y un jabalí salvaje se comió todo tu pan. 🥖🐗 Ahora estás perdido, con hambre y sin recursos para sobrevivir en la naturaleza. 💀🥀")
        else:
            print("💀 Has muerto por dudar demasiado en la aldea.")
    
    elif opcion == 2:
        print("""
Has elegido la opción 2. Punto de Aparición (Bosque🌳)  
El Bosque de los Encuentros...
El azar ha hablado y te encuentras rodeado de troncos de roble y una vegetación tan densa que apenas ves el cielo 🌲. 
El aire huele a pino y a tierra mojada. Consultas tu mapa 🗺️ y confirmas que estás en el corazón del bosque.
Escuchas un crujido de ramas a tu derecha... parece que no estás solo."
Tu Inventario: 🗺️ 1 Mapa | 🥖 3 Panes              
""") 
        print("(LANZAR un trozo de Pan hacia el arbusto) o (CORRER en dirección opuesta hacia lo claro 🏃‍♂️)")
        time.sleep(2)   
        decision2 = input("¿Qué deseas hacer? (lanzar / correr): ").lower()   
        if decision2 == "lanzar":
            print("✨Lanzas un trozo de tu pan hacia el arbusto. De entre las hojas sale un Lobo 🐺 moviendo la cola; se come el pan y decide que eres su nuevo mejor amigo. El lobo te guía por un sendero oculto donde encuentras un Cofre de suministros 📦 con flechas y una armadura de cuero. ¡Has ganado un aliado y equipo nuevo!")
        elif decision2 == "correr":
            print("💀Corres a ciegas entre los árboles, ignorando el mapa 🗺️. De repente, el suelo desaparece bajo tus pies. Has caído en una trampa de foso llena de estacas de madera que un grupo de saqueadores preparó. No hay forma de salir de aquí. GAME OVER: El bosque no perdona a los que huyen por miedo.")
        else:
            print("💀 Has muerto por no decidir qué hacer en el bosque.")

    elif opcion == 3:
        print("""
Has elegido la opción 3. Punto de Aparición (Montaña/Cuevas ⛰️)  
El azar ha decidido tu destino te encuentras en la falda de una montaña colosal ⛰️ cuyas cumbres están cubiertas de nieve perpetua.
El viento sopla con tanta fuerza que casi te arranca el mapa 🗺️ de las manos.
Al mirar hacia arriba, ves una entrada estrecha a una cueva de donde emana un calor extraño, 
pero el camino que bordea el precipicio parece llevar a un antiguo puesto de vigilancia.
Tu Inventario: 🗺️ 1 Mapa | 🥖 3 Panes
""")
        print("(Entrar en la Cueva Humeante 🕳️) o (Seguir el camino del Precipicio 🚠)")
        time.sleep(2)  
        decision3 = input("¿Qué deseas hacer? (entrar / seguir): ").lower() 
        if decision3 == "entrar":
            print("💀Te adentras en la cueva confiando en tu suerte. Sin embargo, el calor no venía de una fogata, sino de un lago de lava 🌋 oculto por una fina capa de piedra. El suelo cede y, antes de que puedas usar tus panes para recuperarte, todo se vuelve rojo. GAME OVER: La montaña reclama una víctima más.")
        elif decision3 == "seguir":
            print("✨Caminas con cuidado pegado a la pared de roca. Al llegar al puesto de vigilancia, encuentras un cofre abandonado con un Catalejo 🔭 y unas Botas de Cuero con Paso Helado. Ahora puedes ver los peligros desde lejos y caminar sobre la nieve sin hundirte. ¡La cima es tuya!")
        else:
            print("💀 Has muerto por congelamiento al no tomar una decisión en la montaña.")

    elif opcion == 4:
        print("""
Has elegido la opción 4. Punto de Aparición (Oceano/Mar🌊)
Abres los ojos y lo primero que sientes es el sabor a sal en tus labios. 
No hay tierra firme a la vista, solo una extensión infinita de agua azul profundo 🌊 que se mueve rítmicamente.
Flotas sobre unos restos de madera, abrazando tu Mapa 🗺️ para que no se moje. Debajo de ti, el fondo marino esconde secretos antiguos
el brillo de un monumento submarino y, un poco más allá, las maderas podridas de un naufragio.
Tu Inventario: 🗺️ 1 Mapa | 🥖 3 Panes
""")
        print("(Bucear hacia el Naufragio ⛵) o (Nadar hacia el Monumento de Piedra 🏛️)")
        time.sleep(2) 
        decision4 = input("¿Qué deseas hacer? (bucear / nadar): ").lower()
        if decision4 == "bucear":
            print("✨Sumerges la cabeza y nadas con fuerza. Logras entrar por una rotura en el casco del barco y abres un cofre: ¡contiene un Casco de Oro ⛑️ con Afinidad Acuática y un mapa del tesoro enterrado! Sales a la superficie justo a tiempo, con los pulmones ardiendo pero con el botín en tus manos. ¡El mar te ha favorecido!")
        elif decision4 == "nadar":
            print("💀Te acercas a la estructura verde, pero un ojo gigante se abre en la pared. Un Guardián 🐡 te apunta con su rayo láser azul. Antes de que puedas dar media vuelta, el rayo te golpea y te deja exhausto bajo el agua. GAME OVER: El océano es un cementerio para los curiosos sin preparación.")
        else:
            print("💀 Has muerto ahogado por no tomar ninguna decisión en el mar.")
   
    elif opcion == 5:
        print("""
Has elegido la opción 5. Punto de Aparición (Tierras Desiertas 🏜️ )
El azar te ha arrojado a un mar de arena infinita que quema a través de tus boots 🏜️. 
El aire ondula por el calor y no hay una sola nube que te proteja del sol implacable ☀️. 
Al consultar tu mapa 🗺️, notas que tus 3 panes 🥖 empiezan a endurecerse por el clima.
En el horizonte, ves dos siluetas: una imponente Pirámide de Arena medio enterrada y, 
hacia el otro lado, un pequeño Pozo de Agua rodeado de arbustos secos.
Tu Inventario: 🗺️ 1 Mapa | 🥖 3 Panes
""")
        print("(Explorar la Pirámide de Arena 🏛️) o (Beber del Pozo de Agua 💧)")
        time.sleep(2)
        decision5 = input("¿Qué deseas hacer? (explorar / beber): ").lower()
        if decision5 == "explorar":
            print("✨Bajas con cuidado a la cámara secreta y evitas pisar la placa de presión del centro. Al abrir los cofres, ¡encuentras Lingotes de Oro 💰 y una Silla de Montar! Logras salir antes de que una tormenta de arena cubra la entrada. ¡Has saqueado la pirámide con éxito!")
        elif decision5 == "beber":
            print("💀Corres desesperado hacia el agua, pero al llegar notas que el pozo está seco y lleno de Cactus 🌵 escondidos bajo la arena. Al intentar buscar humedad, te pinchas profundamente y el ruido atrae a una horda de Cáscaras (zombis del desierto) que te rodean. GAME OVER: El desierto no perdona a los que se dejan engañar por la sed.")
        else:
            print("💀 Has muerto por deshidratación al no tomar una decisión en el desierto.")

    elif opcion == 6: 
        print("""
Has elegido la opción 6. Punto de Aparición (Jardín Floral🌻)              
El azar ha sido generoso y te ha transportado a un valle infinito de colores vibrantes 🌸.
El aroma de miles de flores inunda el aire y el zumbido de las abejas 🐝 trabajando suena como una melodía tranquila. 
Consultas tu mapa 🗺️ y ves que este lugar es inmenso. En medio de un campo de Girasoles 🌻, ves una Colmena rebosante de miel dorada, 
mientras que a lo lejos, una extraña Flor Gigante de pétalos oscuros resalta entre las demás.              
""")
        print("(Recolectar miel de la Colmena 🍯) o (Investigar la Flor Gigante 🌺)")
        time.sleep(2)
        decision6 = input("¿Qué deseas hacer? (recolectar / investigar): ").lower()
        if decision6 == "recolectar":
            print("✨Con movimientos lentos y cuidadosos, logras recoger la miel sin molestar a las abejas. Al combinarla con tu pan, ¡has creado Pan con Miel! 🍯🥖 Esto no solo te llena de energía, sino que te otorga una regeneración mágica que te prepara para cualquier peligro. ¡Has convertido este jardín en tu santuario!")
        elif decision6 == "investigar":
            print("💀Al acercarte a la flor gigante, esta se abre de golpe liberando una nube de polen púrpura 💨. El olor es tan dulce que te marea instantáneamente y tus piernas dejan de responder. Resulta que es una Planta Carnívora gigante disfrazada. GAME OVER: En la naturaleza, lo más brillante suele ser lo más peligroso.")
        else:
            print("💀 Has muerto por alergia extrema al no tomar una decisión en el jardín.")
  
    else:
        print("""Opción no válida.
⚠️ FATAL_ERROR: WORLD_CORRUPTION_DETECTED ⚠️
🌿-🌿-6-;;-2-🌳-🌊-1-1-;;-🏠-5-5-🏜️-🌿-6
--,,,--;;--⛰️-3-3-;;-🌊-4-4-;;-🌊-🌊-🌊
🌿-🌿-6-;;-🏠-1-1-;;-🌳-2-2-;;-🌳-🌳-2
--⛰️-3-⛰️--,,,--;;--🏜️-5-🏜️--,,,--;;
🌊-4-🌊-4-;;-🌿-6-6-;;-🏠-1-1-;;-!!!
⚠️  ERROR AL GENERAR EL MUNDO ⚠️ ... > """)