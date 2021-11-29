def division():
    
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))

    if n2 == 0:
        print("No es posible la división")
    else:
        #redonde de decimales
        print ("{0:.2f}".format(n1/n2))



def tributar():

    edad = int(input("Ingrese su edad"))
    ingresos = float(input("Ingrese sus ingresos"))

    if edad >= 16 and ingresos >= 1000:
        print("Usted debe de tributar")

        return
    else:
        print(" No es necesario que haga el tributo")



def game():
    age = int(input ("Ingrese su edad: "))

    if age <=0: 
        print("no existe esta edad")
        return

    if age <= 4:
        print("Entrada gratis")

    elif age <= 18:
        print("Su pago es de 5 dolares")

    else:
        print ("Supago es de 10 dolares")



game()


#tributar()

#division()

        



  