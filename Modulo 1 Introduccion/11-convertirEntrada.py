#Modificar Tipo de dato de entrada por teclado
# Input siempre va a devolver un tipo de dato tipo string

edad = input('Ingresa tu edad: ')
print(edad)
print(type(edad))


edad_entera = int(edad)
print(edad_entera)
print(type(edad_entera))


altura = input('Ingresa tu altura:')
print(altura)
print(type(altura))

altura_float = float(altura)
print(altura_float)
print(type(altura_float))


autorizacion = input('¿Autorizas el programa? (si/no)')

autorizacion = autorizacion == 'si'

print(autorizacion)