# Operadores logicos
# Para comparar tipos booleanos
# and, or y not Obtenemos un Booleano

#and
print("AND")

resultado_verdadero = True and True
print(resultado_verdadero)

resultado_verdadero = True and True and True and True
print(resultado_verdadero)

resultado_falso = True and False
print(resultado_falso)

resultado_verdadero = True and True and 100 > 20
print(resultado_verdadero)


#or
print("OR")

resultado_verdadero = True or True
print(resultado_verdadero)

resultado_verdadero = True or False
print(resultado_verdadero)

resultado_falso = False or False
print(resultado_falso)

resultado_falso = False or False or 10 > 100
print(resultado_falso)

print("Combinacion de AND y OR usando parentesis")

resultado_verdadero= True and (False or 50>10)
print(resultado_verdadero)


#not
print("NOT")

resultado_verdadero = not False
print(resultado_verdadero)

resultado_falso = not True
print(resultado_falso)