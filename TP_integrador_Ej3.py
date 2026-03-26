# TP integrador – Repetitivas- Condicionales y Secuenciales.
#
# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
#
nombre = ""
option = ""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

# petición y verificación del nombre del operador
while not(nombre.isalpha()):
    nombre = input ('Operador: ')

while option != "5":
    print ('1) Reservar turno \n2) Cancelar turno \n3) Ver agenda del dia \n4) Ver resumen general \n5) Salir')
    option = input ('Opción: ')
    
    #comprobación de opción
    if option > "5" or not(option.isdigit()):
        print('Error: Opción no valida\n')
    elif option == "1":
        dia = ""
        while not(dia.isdigit()):

            print('1)Lunes    2)Martes')
            dia = input ('Dia: ')
            if dia.isalpha() or dia > "2" or dia < "1":
                print ('Error: Opción no valida')
            elif dia == "1":
                paciente = ""
                while not(paciente.isalpha()):
                    paciente = input('Paciente: ')
                    if not(paciente.isalpha):
                        print('Error: ingrese nombre valido')
                        continue

#                   verificando disponibilidad dia lunes
                    if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                        print("Paciente con Turno.")
                    elif lunes1 == "":
                        lunes1 = paciente
                    elif lunes2 == "":
                        lunes2 = paciente
                    elif lunes3 == "":
                        lunes3 = paciente
                    elif lunes4 == "":
                        lunes4 = paciente
                    else:
                        print("dia ocupado.")
            
            elif dia == "2":
                paciente = ""
                while not(paciente.isalpha()):
                    paciente = input('Paciente: ')
                    if not(paciente.isalpha):
                        print('Error: ingrese nombre valido')
                        continue
#                   verificando disponibilidad dia martes
                    if paciente == martes1 or paciente == martes3 or paciente == martes3:
                        print ('Paciente ya cargado.')
                    elif martes1 == "":
                        martes1 = paciente
                    elif martes2 == "":
                        martes2 = paciente
                    elif martes3 == "":
                        martes3 = paciente
                    else:
                        print("dia ocupado")
    
    elif option == "2":
        dia = ""
        while not(dia.isdigit()):

            print('1)Lunes    2)Martes')
            dia = input ('Dia: ')
            if dia.isalpha() or dia > "2" or dia < "1":
                print ('Error: Opción no valida')
            elif dia == "1":
                paciente = ""
                while not(paciente.isalpha()):
                    paciente = input('Paciente: ')
                    
                    if lunes1 == paciente:
                        print ('Cancelado')
                        lunes1 = ""
                    elif lunes2 == paciente:
                        print ('Cancelado')
                        lunes2 = ""
                    elif lunes3 == paciente:
                        print ('Cancelado')
                        lunes3 = ""
                    elif lunes4 == paciente:
                        print ('Cancelado')
                        lunes4 = ""
                    else:
                        print('Paciente no encontrado.')
                        
            elif dia == "2":
                paciente = ""
                while not(paciente.isalpha()):
                    paciente = input('Paciente: ')

                    if martes1 == paciente:
                        print('Cancelado.')
                        martes1 = ""
                    if martes2 == paciente:
                        print('Cancelado.')
                        martes2 = ""
                    if martes3 == paciente:
                        print('Cancelado.')
                        martes3 = ""
                    else:
                        print('Paciente no encontrado.')
    
    elif option == "3":
        dia = ""
        while not (dia.isdigit()):
            print('1) Lunes     2) Martes')
            dia = input('Dia: ')
            if dia.isalpha() or dia > "2" or dia < "1":
                print ('Error: Opción no valida')
    
            elif dia == "1":
                print('Los turnos para el dia Lunes son:')
                if lunes1 == "":
                    print('Turno 1: Libre.')
                else:
                    print(f'Turno 1: {lunes1}')
                if lunes2 == "":
                    print('Turno 2: Libre.')
                else:
                    print(f'Turno 2: {lunes2}')
                if lunes3 == "":
                    print('Turno 3: Libre.')
                else:
                    print(f'Turno 3: {lunes3}')
                if lunes4 == "":
                    print('Turno 4: Libre.')
                else:
                    print(f'Turno 4: {lunes4}')

            elif dia == "2":
                print ('\nLos turnos para el Martes son: ')
                if martes1 == "":
                    print('Turno 1: Libre')
                else:
                    print(f'Turno 1: {martes1}')
                if martes2 == "":
                    print('Turno 2: Libre')
                else:
                    print(f'Turno 2: {martes2}')
                if martes3 == "":
                    print('Turno 3: Libre')
                else:
                    print(f'Turno 3: {martes3}')
        
    elif option == "4":
        lunesOcupado = 0
        martesOcupado = 0
        print('Los turnos para el dia Lunes son:')
        if lunes1 == "":
            print('Turno 1: Libre.')
        else:
            print(f'Turno 1: {lunes1}')
            lunesOcupado +=1
        if lunes2 == "":
            print('Turno 2: Libre.')
        else:
            print(f'Turno 2: {lunes2}')
            lunesOcupado +=1
        if lunes3 == "":
            print('Turno 3: Libre.')
        else:
            print(f'Turno 3: {lunes3}')
            lunesOcupado +=1
        if lunes4 == "":
            print('Turno 4: Libre.')
        else:
            print(f'Turno 4: {lunes4}')
            lunesOcupado +=1

        print ('\nLos turnos para el Martes son: ')
        if martes1 == "":
            print('Turno 1: Libre')
        else:
            print(f'Turno 1: {martes1}')
            martesOcupado += 1
        if martes2 == "":
            print('Turno 2: Libre')
        else:
            print(f'Turno 2: {martes2}')
            martesOcupado += 1
        if martes3 == "":
            print('Turno 3: Libre')
        else:
            print(f'Turno 3: {martes3}')
            martesOcupado += 1

        if lunesOcupado == martesOcupado:
            print('Hay un empate en turnos entre los dias Lunes y Martes')
        elif lunesOcupado > martesOcupado:
            print('El Lunes es el dia con mas turnos')
        else:
            print('El Martes es el dia con mas turnos')
            