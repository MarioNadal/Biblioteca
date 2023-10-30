# Clase Libro
class Libro():
    def __init__(self, titulo, autor, asignatura):
        self.titulo =  titulo
        self.autor = autor
        self.asignastura = asignatura
        self.prestado = False

    def prestar(self):
        if self.prestado:
            print(f"Lo siento el libro {self.titulo} está en préstamo")
        else:
            print(f"Se acaba de prestar el libro {self.titulo}")
            self.prestado = True

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"Se ha devulto el libro {self.titulo}")
        else:
            print(f"El libro {self.titulo} no esta prestado")

quijote = Libro("El Quijote", "Miguel de Cervantes", "IESSAM-01")
cienyears = Libro("Cien años de soledad", "Gabriel García Márquez", "IESSAM-02")

quijote.prestar()
quijote.prestar()
quijote.devolver()
quijote.prestar()
quijote.devolver()
quijote.devolver()


