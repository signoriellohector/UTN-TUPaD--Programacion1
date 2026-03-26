# TP integrador – Repetitivas- Condicionales y Secuenciales.
#
# Ejercicio 4 — “Escape Room: La Bóveda”
#

energia = 100
tiempo = 12
cerradura_abiertas = 0
alarma = False
codigo_parcial = ""
nombre = ""
option = ""
contadorForzar = 0 # contador anti-spam


# petición del nombre y validación 
while not(nombre.isalpha()):
    nombre = input('Agente: ')
    if not(nombre.isalpha) or nombre == "":
        print('Ingrese Nombre valido')

# inicio del juego
while energia >0 and tiempo > 0 and not (cerradura_abiertas >= 3):
    # mostrando estado 
    print(f'\nAgente: {nombre} \nEnergia: {energia}     Tiempo: {tiempo}\nEstado Alarma: {alarma}\nCodigo: {codigo_parcial}')
    print(f'Cerraduras abiertas: {cerradura_abiertas} \nCantidad de forzado: {contadorForzar}\n')

    #Menu
    print('1)Forzar cerradura    2)Hackear panel    3)Descansar')
    option = input('opción: ')
    if not(option.isdigit) or option > "3" or option < "1":
        print ('Opción invalida.')

    elif option == "1": # Forzar Cerradura (costo -20 energía, -2 tiempo)
        contadorForzar +=1

        if contadorForzar < 3:
            if energia < 40:
                energia -= 20
                tiempo -= 2
                numero  = ""
                print ('Riesgo de Alarma.')
                while not(numero.isdigit()):
                    print ('ingrese un numero entre 1 y 3')
                    numero = input('numero: ')
                    
                    #validar numero
                    if not(numero.isdigit()) or numero > "3" or numero < "1":
                        print ('Ingrese numero valido.')
                    
                    # riesgo de alarma
                    elif numero == "3":
                        alarma = True
                        if tiempo <= 3 and not(cerradura_abiertas >= 3) and alarma:
                            break
                    
                    # forzado normal
                    else:
                        cerradura_abiertas += 1
            else:
                energia -= 20
                tiempo -= 2
                cerradura_abiertas += 1
        
        # Regla anti-spam
        elif contadorForzar >= 3:
            energia -= 20
            tiempo -= 2
            alarma = True
            if tiempo <= 3 and not(cerradura_abiertas >= 3) and alarma:
                break
    
    # Hackear panel (costo: -10 energía, -3 tiempo)
    elif option == "2":
        energia -= 10
        tiempo -= 3
        contadorForzar = 0
        for x in range(4):
            codigo_parcial += "A"
            if len(codigo_parcial) >= 8:
                cerradura_abiertas += 1
                codigo_parcial = ""
    
    # Descansar (costo +15 energía (max 100), -1 tiempo, si alarma == True: -10 energía extra)
    elif option == "3":
        energia += 15
        tiempo -= 1
        contadorForzar = 0
        if energia <= 100:
            energia = 100
        if alarma == True:
            energia -= 10

# Fin del juego 

if cerradura_abiertas == 3:
    print ('VICTORIA')

elif tiempo <= 3 and not(cerradura_abiertas >= 3) and alarma:
    print ('DERROTA (bloqueo).')

elif energia <= 0 or tiempo <= 0:
    print ('DERROTA')