# Clase base
class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} - ID: {self.identificacion}")


# Clases derivadas
class Bibliotecario(Persona):
    def __init__(self, nombre, identificacion, seccion):
        super().__init__(nombre, identificacion)
        self.seccion = seccion

    def mostrar_info(self):  # Polimorfismo
        print(f"Bibliotecario: {self.nombre} - Sección: {self.seccion}")


class Usuario(Persona):
    def __init__(self, nombre, identificacion, correo):
        super().__init__(nombre, identificacion)
        self.correo = correo

    def mostrar_info(self):  # Polimorfismo
        print(f"Usuario: {self.nombre} - Correo: {self.correo}")


# Encapsulación
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def mostrar_info(self):
        print(f"Título: {self.__titulo} - Autor: {self.__autor} - ISBN: {self.__isbn}")


# Uso del programa
if __name__ == "__main__":
    # Personalización: información como bibliotecario
    bibliotecario = Bibliotecario("Johnny Vera", "B007", "Tecnología")
    
    # Usuario de ejemplo
    usuario = Usuario("Ana Torres", "U123", "ana.torres@gmail.com")
    
    # Libro de ejemplo
    libro = Libro("Python para Todos", "Charles Severance", "9781492339243")

    # Mostrar información (Demostración de POO)
    bibliotecario.mostrar_info()  # Muestra tu información como bibliotecario
    usuario.mostrar_info()        # Otro ejemplo con usuario
    libro.mostrar_info()          # Encapsulación aplicada
