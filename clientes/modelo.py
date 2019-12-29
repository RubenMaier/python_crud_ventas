import uuid


class Cliente:

    def __init__(self, nombre, empresa, email, rol, uid=None):
        self.nombre = nombre
        self.empresa = empresa
        self.email = email
        self.rol = rol
        # lo primero es un modulo y lo segundo un standard de la industria
        self.uid = uid or uuid.uuid4()

    def atributos_a_diccionario(self):
        # hacemos un diccionario de "clave valor" con los atributos del propio objeto con el método "vars"
        return vars(self)

    @staticmethod  # decorador que nos permite declarar metodos estáticos dentro de nuestra clase
    # lo cual nos permite ejecutar dicho método sin tener una clase instanciada del objeto
    def esquema():  # nos devuelve una lista con los elementos
        return ['nombre', 'empresa', 'email', 'rol', 'uid']
