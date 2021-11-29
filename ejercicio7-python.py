import os
import json

#esta es una lista vacía
persons = []
file_name = 'base_personas.txt'
#manejo de lista, si hay registros los va imprimir si no no

def load_data():
    #cargar en memoria
    base =open(file_name, 'r')
    json_object = json.load(base)
    return list(json_object)


def list_person():
    os.system('cls')
    print(' ------- Listado de personas -------\n')
    print('nº |  Nombre ')
    if (len(persons) > 0):
        for i in range(len(persons)):
            print('-------------------------------')
            print((i + 1), ' | ', persons[i]["name"], persons[i]["last_name"])
    else:
        print('No hay personas registradas')
    print('\n')
    os.system('pause')

def add_person():

        os.system('cls')
        name = input('Ingrese el nombre: ')
        last_name = input('Ingreso el apellido: ')
        email = input('Ingrese el correo: ')
        salary = input('Ingrese el salario $: ')
        phone = input('Ingrese el numero telefonico: ')
        address = input('Ingrese la dirección: ')
        dui = input('Ingrese el numero de identificación personal: ')

        #creanso un diccionario
        person = { #clave  valor
                 'name': name,
                 'last_name' : last_name,
                 'email' : email,
                 'salary': salary,
                 'phone' : phone,
                 'address' : address,
                 'dui': dui

        }
        persons.append(person)
        #este es un adaptador
        #json_oject en formato json para que lo pueda reconocer los valores
        json_object = json.dumps(persons, indent = 4)
        #que obra el archivo txt en modo de escritura
        with open(file_name, 'w') as base:
             base.write(json_object)
             base.close()
    
        os.system('pause')


def delete_person():
    os.system('cls')
    dui = input('Ingrese el DUI de la persona: ')
    for person in persons:
        if dui.lower() in person['dui'].lower():
            print('persona a eliminar: ',person['name'])
            elimniar = input('¿Desea eliminar? (si/no): ')
            if elimniar == 'si':
                persons.remove(person)
                print('Persona eliminada...')
    os.system('pause')



op = ''
persons = load_data()
while(op != 'exit'):
    os.system('cls')
    print('------- Menu -------')
    print('(1)..... Listar personas')
    print('(2)..... Agregar personas')
    print('(3)..... eliminar persina')
    print('(exit).. Salir')
    print('\n')
    op = input('Ingrese una opción: ')
    if op == '1':
        list_person()
    elif op == '2':
        add_person()
    elif op == '3':
        delete_person()
    elif op == 'exit':
        print('Fin del programa')
    else:
        print('Opción no válida')
        os.system('pause')