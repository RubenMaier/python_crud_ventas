import sys


clientes = [
    {
        'nombre': 'pablo',
        'empresa': 'google',
        'correo': 'pablo@google.com',
        'rol': 'ingeniero en software'
    },
    {
        'nombre': 'ricardo',
        'empresa': 'facebook',
        'correo': 'ricardo@facegook.com',
        'rol': 'ingeniero electronico'
    }
]


def crear_clientes(nuevo_cliente):
    global clientes
    if cliente not in clientes:
        clientes.append(nuevo_cliente)
        print('{} fue creado exitosamente'.format(nuevo_cliente.nombre))
    else:
        print('{} ya esta en la lista de clientes'.format(nuevo_cliente.nombre))


def listar_clientes():
    global clientes
    for indice, cliente in enumerate(clientes):
        print('{}: {}'.format(indice, cliente))


def _bienvenido():
    print('BIENVENIDO A VENTAS')
    print('*' * 50)
    print('Que quieres hacer hoy?')
    print('[C]rear cliente')
    print('[A]ctualizar cliente')
    print('[B]orrar cliente')
    print('[E]ncontrar cliente')
    print('[L]istar clientes')


def borrar_cliente(nombre):
    global clientes
    if nombre in clientes:
        clientes.remove(nombre)
        print('{} fue borrado con exito'.format(nombre))
    else:
        print('No existe {} en nuestra lista'.format(nombre))


def obtener_cliente():
    nombre = None
    while not nombre:
        nombre = input('Ingrese el nombre: ')
        if nombre == 'salir':
            nombre = None
            break
    if not nombre:
        sys.exit()
    return nombre


def actualizar_cliente(nombre, nombre_nuevo):
    global clientes
    if nombre in clientes:
        indice = clientes.index(nombre)
        clientes[indice] = nombre_nuevo
    else:
        print('El cliente no esta en la lista de clientes')


def encontrar_cliente(nombre):
    for cliente in clientes:
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
            print('El cliente esta en la lista')
        else:
            print('El cliente no esta en nuestra lista')
    elif comando == 'L':
        listar_clientes()
    else:
        print('Comando invalido')
