from typing import Counter


def change_letters():
    name = input("Ingrese su nombre completo: ")


    print (name.lower())
    print (name.upper())
    print (name.capitalize())      
    print (name.swapcase())   
    print (name.title())


def longitud():
   # X="Karen Montoya"
    #print(len(X))
    
    name= input("Ingrese su nombre: ")
    print("nombre tiene: ")
    print(len(name.replace(' ','')))

    

longitud()
#change_letters()karen

