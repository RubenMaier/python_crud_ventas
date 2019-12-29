import click

# modificamos los comandos dentro del grupo clientes
# definimos nuestros comandos básicos


from clientes.servicios import ServiciosClientes
from clientes.modelo import Cliente


@click.group()  # con esto los convertimos en comandos de click
def clientes():
    """Administrador de ciclo de vida de clientes"""
    pass


@clientes.command()
@click.option(
    '-n',  # abreviación
    '--nombre',  # nombre completo del comando
    type=str,  #  tipo de dato de entrada
    prompt=True,  # si no viene el nombre incluido, la consola se lo pide
    help='El nombre del cliente')  # mensaje de ayuda
@click.option(
    '-e',
    '--empresa',
    type=str,
    prompt=True,
    help='La empresa del cliente')
@click.option(
    '-em',
    '--email',
    type=str,
    prompt=True,
    help='El email del cliente')
@click.option(
    '-r',
    '--rol',
    type=str,
    prompt=True,
    help='El rol del cliente')
@click.pass_context
def crear(contexto, nombre, empresa, email, rol):
    """ Crea un nuevo cliente """
    cliente = Cliente(nombre, empresa, email, rol)
    servicios_cliente = ServiciosClientes(contexto.obj['tabla_clientes'])
    servicios_cliente.crear_cliente(cliente)


@clientes.command()
@click.pass_context
def listar(contexto):
    """Lista todo los clientes"""
    servicios_cliente = ServiciosClientes(contexto.obj['tabla_clientes'])
    lista_clientes = servicios_cliente.listar_clientes()
    # para imprimir algo en la consola hacemos uso de click.echo y no de print porque la forma en que funciona...
    # la libreria click en los distintos SO varia, y asi aseguramos mostrar todo bajo un mismo formato
    click.echo(' ID | NOMBRE | EMPRESA | EMAIL | ROL')
    click.echo('*' * 100)
    for cliente in lista_clientes:
        click.echo('{uid} | {nombre} | {empresa} | {email} | {rol}'.format(
            uid=cliente['uid'],
            nombre=cliente['nombre'],
            empresa=cliente['empresa'],
            email=cliente['email'],
            rol=cliente['rol']))


@clientes.command()
@click.argument(
    'cliente_id',
    type=str)
@click.pass_context
def actualizar(contexto, cliente_id):
    """Actualiza el cliente"""
    servicio_cliente = ServiciosClientes(contexto.obj['tabla_clientes'])
    cliente = _buscar_cliente_por_id(servicio_cliente, cliente_id)
    if cliente != None:  # si la lista no es vacía entonces...
        # creamos un flujo de actualización
        # desempaqueto al primer elemento de la lista que es el cliente que quiero actualizar
        # debo instanciar al cliente en su clase Clientes por lo que le pasamos la referencia como: **cliente[0]
        cliente_actualizado = _flujo_de_cliente_actualizado(
            _diccionario_a_objeto(cliente))
        servicio_cliente.actualizar_cliente(cliente_actualizado)
        click.echo('El cliente fue actualizado')
    else:
        click.echo('El cliente no fue encontrado')


@clientes.command()
@click.argument(
    'cliente_id',
    type=str)
@click.pass_context
def eliminar(contexto, cliente_id):
    """Elimina el cliente"""
    servicio_cliente = ServiciosClientes(contexto.obj['tabla_clientes'])
    cliente = _buscar_cliente_por_id(servicio_cliente, cliente_id)
    print(cliente)
    if cliente != None:  # si la lista no es vacía entonces...
        servicio_cliente.borrar_cliente(_diccionario_a_objeto(cliente))
        click.echo('El cliente fue eliminado')
    else:
        click.echo('El cliente no fue encontrado')


def _buscar_cliente_por_id(servicio_cliente, cliente_id):
    lista_clientes = servicio_cliente.listar_clientes()
    # queremos al cliente de todos los clientes que se encuentren en la lista de clientes...
    # que cumpla con la condición de que su id es la que nos pasaron por parametro
    cliente = [
        cliente for cliente in lista_clientes if cliente['uid'] == cliente_id]
    if len(cliente) > 0:
        return cliente[0]
    return None


def _diccionario_a_objeto(cliente_dic):
    return Cliente(**cliente_dic)


def _flujo_de_cliente_actualizado(cliente):
    click.echo('Deja vacío si no quiere modificar el valor')
    cliente.nombre = click.prompt(
        'Nuevo nombre', type=str, default=cliente.nombre)
    cliente.empresa = click.prompt(
        'Nuevo empresa', type=str, default=cliente.empresa)
    cliente.email = click.prompt(
        'Nuevo email', type=str, default=cliente.email)
    cliente.rol = click.prompt(
        'Nuevo rol', type=str, default=cliente.rol)
    return cliente


comandos_declarados = clientes
