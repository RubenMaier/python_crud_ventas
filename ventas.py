import click

from clientes import comandos

TABLA_CLIENTES = '.clientes.csv'


@click.group()  # con este decorador indicamos que este será el punto de entrada
@click.pass_context  #  con este decorador obtenemos un objeto contexto
def punto_de_entrada(contexto):
    # inicializamos este objeto contexto como un diccionario vacío
    contexto.obj = {}
    # le agregamos la clave tabla_clientes con el valor TABLA_CLIENTES
    contexto.obj['tabla_clientes'] = TABLA_CLIENTES


punto_de_entrada.add_command(comandos.comandos_declarados)
