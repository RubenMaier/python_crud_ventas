clientes='pablo,ricardo,'

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
    print('[B]orrar cliente')

if __name__ == '__main__':
    _bienvenido()
    comando = input()
    if comando == 'C':
        nombre_cliente = input('Cual es el nombre del cliente? ')
        crear_clientes(nombre_cliente)
        listar_clientes()
    elif comando == 'D':
        pass
    else:
        print('Comando invalido')