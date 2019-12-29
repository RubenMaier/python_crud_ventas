# modulo que me permite trabajar comodo con el formato de archivo csv (comma-separated values)
import csv
# modulo que me permite manejar funcionalidades del sistema operativo
import os

from clientes.modelo import Cliente


class ServiciosClientes:
    def __init__(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla  # es nuestro csv la tabla

    def crear_cliente(self, cliente):
        # abrimos el archivo
        with open(self.nombre_tabla, mode='a') as archivo:
            # creamos el objeto de escritura con formato csv respetando el esquema de columnas definido en la clase "Clientes"
            # para eso hacemos uso de la clase csv con su método DictWriter declarando el archivo y el esquema
            # csv.DictWriter(archivo, esquema de columnas del csv)
            escritura = csv.DictWriter(archivo, Cliente.esquema())
            # añadimos una objeto "cliente" con sus atributos en formato diccionario
            escritura.writerow(cliente.atributos_a_diccionario())

    def listar_clientes(self):  # vemos que tipos de clientes tenemos
        with open(self.nombre_tabla, mode='r') as archivo:
            lectura = csv.DictReader(archivo, Cliente.esquema())
            # como el resultado es un iterable lo convertimos en una lista y lo devolvemos
            return list(lectura)

    def actualizar_cliente(self, cliente_actualizado):
        clientes = self.listar_clientes()
        # lista auxiliar para ciclar entre los clientes para encontrar al que se necesita actualizar y...
        # tener al final como resultado la lista con los no modificados mas el modificado
        clientes_actualizados = []
        for cliente in clientes:
            if cliente['uid'] == cliente_actualizado.uid:
                # añadimos solo el cliente actualizado a la lista
                clientes_actualizados.append(
                    cliente_actualizado.atributos_a_diccionario())
            else:
                # añadimos todos los clientes que no fueron modificados
                clientes_actualizados.append(cliente)
        self._guardar_en_disco(clientes_actualizados)

    def borrar_cliente(self, cliente_a_borrar):
        clientes = self.listar_clientes()
        clientes_resultantes = []
        for cliente in clientes:
            if cliente['uid'] != cliente_a_borrar.uid:
                clientes_resultantes.append(cliente)
        self._guardar_en_disco(clientes_resultantes)

    def _guardar_en_disco(self, clientes):
        # esta tabla temporal existe porque ya abrimos el archivo y no podemos volverlo a escribir porque...
        # lo abrimos en modo lectura cuando obtuvimos nuestra lista de clientes
        nombre_tabla_temporal = self.nombre_tabla + '.tmp'
        # escribimos un archivo csv en disco con los clientes que nos pasaron por parámetro
        with open(nombre_tabla_temporal, mode='w') as archivo:
            escritura = csv.DictWriter(archivo, Cliente.esquema())
            escritura.writerows(clientes)
        # borro el archivo original
        os.remove(self.nombre_tabla)
        # renombro la tabla temporal al nombre original
        os.rename(nombre_tabla_temporal, self.nombre_tabla)
