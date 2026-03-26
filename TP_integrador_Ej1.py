# TP integrador – Repetitivas- Condicionales y Secuenciales.
#
# Ejercicio 1— “Caja del Kiosco”
#

#inicializando las variable
nombre = ""
cantidad = ""
total = 0.0
totalSin = 0
opciones = "SNsn"

# pidiendo el ingreso del nombre y comprobando que no sea nombre vacío y solo contenga letras
while nombre.isalpha() == False:
    nombre= input('Cliente: ')
    if nombre == "":
        print('Error: nombre de cliente Vacío')

# pidiendo el ingreso de la cantidad de productos y comprobando que sea un numero entero positivo 
while cantidad.isdigit() == False:
    cantidad = input('Cantidad de productos: ')


cantidad = int(cantidad)

# ingresando y validando los precios de productos
for x in range(cantidad):
    precio = ""
    descuento = ""
    while precio.isdigit() == False:
        precio = input(f'producto {x+1} - precio: ')
        # validando si poseen descuento y sumándolo al total
        while (descuento in opciones) == False or descuento.isalpha() == False:
            descuento = input('Descuento (S/N): ')
            if descuento in "sS":
                total += (int(precio) * 0.9)
                totalSin += int(precio)
            elif descuento in "nN":
                total += int(precio)
                totalSin += int(precio)
        
# calculando el ahorro y promedio
ahorro = totalSin - total
promedio = total / cantidad

print (f'Total sin descuentos: {totalSin}')
print (f'Total con descuentos: {total:.2f}')
print (f'Ahorro: {ahorro}')
print (f'Promedio por producto: {promedio:.2f}')

