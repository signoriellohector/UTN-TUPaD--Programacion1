# TP integrador – Repetitivas- Condicionales y Secuenciales.
#
# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#

UsuarioCorrecto = "alumno"
Clave = "python123"
intentos = 0
opcion = ""

while intentos < 3:
    print(f'intento {intentos + 1}/3')
    usuario = input ('Ingrese el usuario: ')
    clave = input('Ingrese la Clave: ')
    intentos += 1
    if usuario == UsuarioCorrecto and clave == Clave:
      print('Acceso Concedido.')
      break
    else:
        print('Credenciales inválidas')


if intentos < 3:
    while opcion != "4":
        print('\n 1) Estado   2) Cambiar clave  3) Mensaje  4) Salir')
        opcion = input('opción: ')
        if not(opcion.isdigit()):
            print('Error: ingrese un número válido.')
        elif opcion > "4":
            print('Error: opción fuera de rango.')
        elif opcion == "1":
            print('Inscripto')
        elif opcion == "2":
            nuevaClave = input('Ingrese Clave nueva: ')
            claveConf = input ('Ingrese confirmación de clave: ')
            if nuevaClave != claveConf:
                print('Error: Clave nueva y la confirmación no coinciden.')
            elif (len(nuevaClave) < 6):
                print('Error: mínimo 6 caracteres.')
        elif opcion == "3":
            print('Puede ser duro pero siempre hay una solución')
else:
    print ('Cuenta bloqueada.')