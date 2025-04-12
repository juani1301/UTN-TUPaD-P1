#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input ("por favor ingrese su edad"))
           
if edad > 18:
    print ("es mayor de edad")



#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

NOTA_PARA_APROBAR = 6

nota = int(input("ingrese nota de calificacion: "))

if nota >= NOTA_PARA_APROBAR:
    print ("aprobado")
elif nota:
    print ("desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par" # . Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("ingrese un numero: "))

if numero % 2 == 0:
    print ("el numero es PAR")
else: 
    print ("el numero es IMPAR")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ●# Niño/a: menor de 12 años.
# ●# Adolescente: mayor o igual que 12 años y menor que 18 años.
# ●# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ●# Adulto/a: mayor o igual que 30 años.

edad = int(input("ingrese su edad: "))

if 0 < edad < 12:
    print ("ud. es niño")
elif 12 <= edad < 18:
    print ("Ud. es adolescente")
elif 18 <= edad < 30:
    print (" Ud. es un adulto/a joven ")   
elif edad >= 30:
    print (" Ud. es un adulto/a mayor ") 


#     5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"# . Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

pss = input ("Introduzca una contraseña que tenga entre 8 y 14 caracteres: ")

if  8<= len (pss) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


import statistics as st 


import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media =  (st.fmean (numeros_aleatorios))
mediana = (st.median (numeros_aleatorios))
moda = (st.mode (numeros_aleatorios))

print ("la media es: ", media)
print ("la mediana es: ", mediana)

if media > mediana:
    print ("sesgo positivo")

elif media < mediana:
    print ("sesgo negativo")
elif media == mediana == moda:
    print (" sin sesgo")