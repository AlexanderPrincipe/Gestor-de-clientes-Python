import re
import gestor.helpers as helpers


class Client:

    nombre: str
    apellido: str
    dni: str

    def __init__(self, nombre: str, apellido: str, dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellido}"


class Manager:

    clients: list = []

    @staticmethod
    def show_client(client: Client):
        print(client)

    @staticmethod
    def show_clients():
        if Manager.clients == []:
            print("No hay clients disponibles.")
        else:
            for client in Manager.clients:
                Manager.show_client(client)

    @staticmethod
    def add():

        print('Introduce nombre (De 2 a 30 caracteres)')
        nombre = helpers.input_text(2, 30)
        print('Introduce apellido (De 2 a 30 caracteres)')
        apellido = helpers.input_text(2, 30)
        while True:
            print("Introduce DNI (2 números y 1 carácter en mayúscula)")
            dni = helpers.input_text(3, 3)
            if Manager.is_valid(dni):
                Manager.clients.append(Client(nombre, apellido, dni))
                break
            else:
                print("DNI incorrecto o en uso")
                dni = None

    @staticmethod
    def is_valid(dni: str):
        if not re.match('[0-9]{2}[A-Z]$', dni):
            return False
        for client in Manager.clients:
            if client.dni == dni:
                return False
        return True

    @staticmethod
    def find():
        dni = input("Introduce el dni del client\n> ")
        for i, client in enumerate(Manager.clients):
            if client.dni == dni:
                Manager.show_client(client)
                return i, client
        print("No se ha encontrado ningún client con ese DNI")
        return None, None

    @staticmethod
    def delete():
        i, client = Manager.find()
        if client:
            client = Manager.clients.pop(i)
            return True
        return False

    @staticmethod
    def edit():
        i, client = Manager.find()
        if client:
            print(f"Introduce nuevo nombre ({client.nombre})")
            Manager.clients[i].nombre = helpers.input_text(2, 30)
            print(f"Introduce nuevo apellido ({client.apellido})")
            Manager.clients[i].apellido = helpers.input_text(2, 30)
            return True
        return False