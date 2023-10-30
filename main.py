# Clase Libro
class Libro():
    def __init__(self, titulo, autor, asignatura):
        self.titulo = titulo
        self.autor = autor
        self.asignastura = asignatura
        self.prestado = False
        self.prestadoA = None

    def prestar(self, persona):
        if self.prestado:
            print(f"Lo siento, el libro {self.titulo} está en préstamo a {self.prestadoA.nombre}")
        else:
            self.prestado = True
            self.prestadoA = persona
            print(f"Se acaba de prestar el libro {self.titulo} a {self.prestadoA.nombre}")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.prestadoA.nombre} ha devulto el libro {self.titulo}")
        else:
            print(f"El libro {self.titulo} no esta prestado")


class Persona():
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni


quijote = Libro("El Quijote", "Miguel de Cervantes", "IESSAM-01")
cienyears = Libro("Cien años de soledad", "Gabriel García Márquez", "IESSAM-02")
alicia = Persona("Alicia", "Anderson", "29345778S")

quijote.prestar(alicia)
quijote.prestar(alicia)
quijote.devolver()
quijote.prestar(alicia)
quijote.devolver()
quijote.devolver()
