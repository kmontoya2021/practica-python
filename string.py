myStr = "hello mundo car"

print(dir(myStr))

#pone la frase en mayuscula
print(myStr.upper())

#pone la frase en minuscula
print(myStr.lower())

print(myStr.swapcase())
#pone mayuscula y minuscula
print(myStr.capitalize())
#reemplaza la primera palabra con la segunda y luego la pasa a mayuscula
print(myStr.replace("hola", "Karen").upper())
#cuanta cuantas l hay en la frase
print(myStr.count("l"))
#busca al inicio de la frase si esta la palabra "hola" y da un tru o false
print(myStr.startswith("hola"))
#busca si al final hay esta la palabra "mundo" y devuelve un verdadero o falso
print(myStr.endswith("mundo"))
#separa cada palabra de la frase
print(myStr.split())
#pone la posición de la letra que se ponga en los parentesis
print(myStr.find("o" ))
#tamaño de la frase
print(myStr.__len__( ))
#para saber donde esta el indice de la letra e, se inicia el conteo con cero
print(myStr.index("e"))

#pregunta si es numerico
print(myStr.isnumeric())
#pregunta si es un alfanumerico
print(myStr.isalpha( ))
#imprimir lo que esta en la posición del vector
print(myStr[2])
print(myStr[4])
#comienza del orden inverso
print(myStr[-2])
