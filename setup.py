from setuptools import setup

setup(
    name='ventas',  # nombre para ejecutar el programa
    version='0.1',
    py_modules=['ventas'],
    install_requires=[  # dependencias
        'Click'],
    entry_points='''
        [console_scripts]
        ventas=ventas:punto_de_entrada
    ''')  #  desde donde se ejecuta
