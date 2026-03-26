# TP integrador – Repetitivas- Condicionales y Secuenciales.
#
# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
#

import random
# inicializando variables
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3 
damage_base_gladiador = 15 
damage_base_enemigo = 12
turno_gladiador=True

print('--- BIENVENIDO A LA ARENA ---')

nombre_gladiador=input("Ingrese el nombre del gladiador: ")

# petición y validación del nombre
while nombre_gladiador=="" or not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador=input("Ingrese el nombre del gladiador: ")

nombre_gladiador=nombre_gladiador.capitalize()

print ('=== INICIO DEL COMBATE ===')
# Comienzo del juego 
while vida_gladiador>0 and vida_enemigo>0:
    if turno_gladiador:
        #Estado actual
        print(f"{nombre_gladiador} HP ({vida_gladiador}) VS Enemigo HP ({vida_enemigo}) | Pociones: {pociones_vida}")

        # menu del juego
        while True:
            opcion=""
            while opcion=="" or not opcion.isdigit():
                opcion=input('''Indique la acción a realizar:\n
                1)Ataque pesado
                2)Ataque por ráfaga
                3)Curar
                ''')
                if opcion == "" or not (opcion.isdigit()):
                    print("Error: Solo se permiten números")

            if opcion == "1":
                if vida_enemigo<20:
                    vida_enemigo=vida_enemigo - 1.5*damage_base_gladiador
                    print(f"Atacaste al enemigo por {1.5*damage_base_gladiador} puntos de daño")
                else:
                    vida_enemigo=vida_enemigo - damage_base_gladiador
                    print(f"Atacaste al enemigo por {damage_base_gladiador} puntos de daño")

                turno_gladiador=False
                break
            
            elif opcion == "2":
                rafaga=random.randint(1,4)
                for x in range(rafaga):
                    vida_enemigo-=5
                    print("> Golpe conectado por 5 de daño")

                turno_gladiador=False
                break
            
            elif opcion == "3":
                if pociones_vida>0:
                    vida_gladiador=vida_gladiador+30
                    pociones_vida-=1
                    print(f"Te curaste, tu vida sube a {vida_gladiador}")
                    print(f"Las pociones de cura quedan en {pociones_vida} pociones restantes.")
                else:
                    print("No dispone de mas pociones de vida")
                    print("Pierdes el turno")

                turno_gladiador=False
                break
            
            else:
                print("La opción ingresada no es valida")
                print("Intente de nuevo")
    else:
        print("\nTurno de ataque del enemigo!!")
        vida_gladiador= vida_gladiador - damage_base_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador=True
        print('\n === Nuevo Turno === \n')

# fin del juego 
if vida_gladiador>0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print(f"DERROTA. Has caído en combate.")
