# Información

 Esté programa es un **CRUD** básico donde se busca implementar los conceptos básicos y fundamentales de Python. Su desarrollo se implementa bajo el paradigma de **POO** y utilizando la [librería click]([https://pypi.org/project/click/](https://pypi.org/project/click/)).
 
En los branch, se puede acceder a la misma implementación desarrollada con distintas herramientas del lenguaje, las cuales fueron resultado de un aprendizaje iterativo incremental desde los conceptos más básicos a los mas frecuentes en la industria.

- [branch básico](https://github.com/RubenMaier/python_crud_ventas/tree/basico)
- [branch lista_básico](https://github.com/RubenMaier/python_crud_ventas/tree/lista_basico)
- [branch lista_diccionario](https://github.com/RubenMaier/python_crud_ventas/tree/lista_diccionario)


# Instalación

Una vez clonado el repositorio se recomienda crear un **entorno virtual** con **Python 3** donde correr el programa. Se debe ejecutar:
```sh
$ virtualenv --python=python3 venv
```
Luego activamos el entorno:
```sh
$ source venv/bin/activate
```
Y finalmente instalamos el programa (estando dentro del directorio clonado):
```sh
$ pip install --editable .
```