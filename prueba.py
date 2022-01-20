print("Hola mundo")

variable = "Hola Dani"
variable_dos = 19
variable_tres = True 
variable_cuatro = print

print(variable)

# Hola esto es un comentario

snake_case = "Esta es la convencion de escritura en Python"

#Funcion type para saber el tipo de variable
print(type(variable))
print(type(variable_dos))
print(type(variable_tres))
#Puedes pasar funciones a variables 
#A la variable cuatro le paso la funcion de imprimir
variable_cuatro(variable)

#Concatenar variables de distinto tipo
#Concatenar String y numeros pasando el numero a String
print("hola"+str(variable_dos))

#Multiplicar palabras
print("hola"*3)

#Implementar metodos a cadenas directamente sin usar objetos
cadena="Ejemplo de cadena"

print(cadena.split(" "))
cadena_nueva=cadena.split(" ")
print(cadena_nueva)
#print(cadena_nueva.join("-"))

print("#################################")
print("##LISTAS")

lista = ["Ejemplo", "de lista", 12345, 5.5, ["con", "cosas"]]##Las listas son agrupaciones de valores mutables se definen con []

print(lista[-2])#Para empezar la lista desde el final ponerlo en negativo
print(lista[2])
print("Tamaño de la lista =" + str(len(lista)))
print("#################################")
#Extraer partes la lista
lista_numeros=[1,2,3,4,5]

print(lista_numeros[1:3])#Devuelve los numeros entre el 1 y el 3, los ":" -> hasta
print(lista_numeros[:3])

#Añadir valores a la lista
lista_numeros.append(6)
print(lista_numeros)
#Concatenar listas
lista_concatenada= [1,4] + [6,7]
print(lista_concatenada)
lista_concatenada.reverse()#Revertir el orden de la lista
print(lista_concatenada)

print("##Tupla")
tupla=(1,2,5,8,"ey","adios")#Las tuplas solo se pueden consultar pero no modificarlas se definen con ()
print(tupla[3])
print(tupla.index(1))


print("##Conjuntos")
##Los conjuntos son mutables se pueden sacar y meter valores
#pero no existe ordenacion y no se pueden consultar se definen con {}

conjunto={"Hola",4,6,0,"adios"}#Ordena la lista aleatoriamente 
print(conjunto)
conjunto.add(3.3)
conjunto.add("wawa")
print(conjunto)

print("##Diccionarios o mapas")#Secuencia de elementos almacenados como pares de "clave : valor"
diccionario = {"lenguaje":"Python", "versión":3.10, "tipo":"Interpretado"}
print(diccionario)

print(diccionario["lenguaje"])#Devuelve el valor de la clave

diccionario["lenguaje"]="Java" #Modificar el valor de la clave
print(diccionario["lenguaje"])

print(len(diccionario))

###################################################
print("##Condicionales")
a=5
b=3
#Condi 1
if a>b :
    print("A es mayor")

#Condi 2
if a==b :
    print("Son iguales")
else :
    print("No son iguales")

#Condi 3
if a==b :
    print("Iguales")
if a<b :
    print("No son iguales y A es menor que B")
else : 
    print("A mayor que B")

print("##Bucles")
#While
x=1
while x<=10:
    print(x)
    x+=1

print(" ")
y=12
while y<=10 :
    print(y)
    y +=1
else:
    print(y)

print("##FOR")
#FOR
nombres = ["Ana","Juan","Jaime"]

for nombre in nombres:
    print(nombre)


