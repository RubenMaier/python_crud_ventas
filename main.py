import sys


clientes = 'pablo,ricardo,'


def crear_clientes(nombre):
    global clientes
    if nombre not in clientes:
        clientes += nombre
        _agregar_coma()
    else:
        print('El cliente ya esta en la lista de clientes')


def listar_clientes():
    global clientes
    print(clientes)


def _agregar_coma():
    global clientes
    clientes += ','


def _bienvenido():
    print('BIENVENIDO A VENTAS')
    print('*' * 50)
    print('Que quieres hacer hoy?')
    print('[C]rear cliente')
    print('[A]ctualizar cliente')
    print('[B]orrar cliente')
    print('[E]ncontrar cliente')


def borrar_cliente(nombre):
    global clientes
    if nombre in clientes:
        clientes = clientes.remplace(nombre + ',', '')
    else:
        print('No existe ese cliente en nuestra lista')


def obtener_cliente():
    nombre = None
    while not nombre:
        nombre = input('Cual es el nombre del cliente que quiere modificar? ')
        if nombre == 'salir':
            nombre = None
            break
    if not nombre:
        sys.exit()
    return nombre


def actualizar_cliente(nombre, nombre_nuevo):
    global clientes
    if nombre in clientes:
        clientes = clientes.replace(nombre + ',', nombre_nuevo + ',')
    else:
        print('El cliente no esta en la lista de clientes')


def encontrar_cliente(nombre):
    for cliente in clientes.split(','):
        if cliente != nombre:
            continue
        else:
            return True


if __name__ == '__main__':
    _bienvenido()
    comando = input('Ingrese el comando: ').upper()
    if comando == 'C':
        listar_clientes()
        crear_clientes(obtener_cliente())
        listar_clientes()
    elif comando == 'B':
        borrar_cliente(obtener_cliente())
        listar_clientes()
    elif comando == 'A':
        nombre_nuevo = input('Cual es el nuevo nombre? ')
        actualizar_cliente(obtener_cliente(), nombre_nuevo)
        listar_clientes()
    elif comando == 'E':
        cliente = encontrar_cliente(obtener_cliente())
        if cliente:
            print('El cliente está en la lista')
        else:
            print('El cliente no esta en nuestra lista')
    else:
        print('Comando invalido')
