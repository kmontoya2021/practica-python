import os
import json
import datetime
import requests

#esta es una lista vacía
persons = []
file_name = 'base_personas.txt'
#manejo de lista, si hay registros los va imprimir si no no

def load_data():
    #cargar en memoria    r= segnifica lectura
    base =open(file_name, 'r')
    json_object = json.load(base)
    return list(json_object)

#Reescribir en los campos del archivo creado    w= significa escritura
def write_to_file():
    json_object = json.dumps(persons, indent=4)
    with open(file_name, 'w') as base:
        base.write(json_object)
        base.close()


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
                 'dui': dui,
                 'date': date

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



def refresh_person():
    modificar =""
    os.system('cls')
    dui_persona = input('Ingrese el DUI de la persona a modificar: ')
    for i in persons:
        if dui_persona == i['dui']:
            modificar = input('¿Desea modificar dato? (si/no): ')    
            if modificar == 'si':
                name =  input('Ingrese nombre: ')    
                i['name'] =  name if name != "" else i['name']
                apellido = input('Ingrese apellido: ')  
                i['last_name'] =  apellido if apellido != "" else i['last_name']
                correo = input('Ingrese nuevoa dirección de correo: ')
                i['email'] = correo if correo != "" else i['email']
                salario = input('Ingrese valor de salario: ')
                i['salary'] = salario if salario != "" else i['salary']
                telefono = input('Ingrese numero de telefono: ')
                i['phone'] = telefono if telefono != "" else i['phone']
                direccion = input('Ingrese nueva dirección: ')
                i['address'] = direccion if direccion != "" else i['address']
                dui = input('Ingrese número de DUI: ')
                i['dui'] = dui if dui != "" else i['dui']
                write_to_file()
                print('campo modificado')
                os.system('pause')
                return 
            else:
                return


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

def show_person():
    os.system('cls')
    dui = input('Ingrese el dui')
    for person in persons:
        if person['dui'] == dui:
            print('----- información ------')
            print('Nombre: ', person['name'])
            print('Apellido: ', person['last_name'])
            print('Correo: ', person['email'])
            print('Salario: ', person['salary'])
            print('Telefono: ', person['phone'])
            print('Dierección: ', person['address'])
            print('Dui ', person['dui'])
            print('Fecha de ingreso: ', person['date'])
            os.system('pause')
            return
    print('Persona no encontrada')
    os.system('pause')

def update_fecha():
    x = datetime.datetime.now()
    for person in persons:
        person['date'] = x.strftime('%d-%m-%y')
        write_to_file()
    print('Se han actualizado las fechas de los registros')
    os.system('pause')  

def get_data():
    data = requests.get('https://jsonplaceholder.typicode.com/users/')
    if data.status_code == 200:
        users = list(json.loads(data.text))
        for user in users:
            print(user['id'], user['name'])
            print (user['id'], 'Nombre: ', user ['name'].split(' ')[0])
            print (user['id'], 'Apellido: ', user ['name'].split(' ')[1])
    else:
        print('Eror de conexión')
        os.system('PAUSE')



op = ''
persons = load_data()
while(op != 'exit'):
    os.system('cls')
    print('------- Menu -------')
    print('(1)..... Listar personas')
    print('(2)..... Agregar personas')
    print('(3)..... Modificar datos de persona')
    print('(4)..... eliminar persona')
    print('(5)..... Mostrar persona')
    print('(6)..... Actualizar fecha')
    print('(7)..... carga de datos en la web')
    print('(exit).. Salir')
    print('\n')
    op = input('Ingrese una opción: ')
    if op == '1':
        list_person()
    elif op == '2':
        add_person()
    elif op == '3':
        refresh_person()         
    elif op == '4':
        delete_person()
    elif op == '5':
        show_person()
    elif op == '6':
        update_fecha()
    elif op == '7':
        get_data()
    elif op == 'exit':
        print('Fin del programa')
    else:
        print('Opción no válida')
        os.system('pause')