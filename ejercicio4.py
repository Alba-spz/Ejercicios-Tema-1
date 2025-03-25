from collections import deque

# Inicializamos la cola como un deque vacío
misiones = deque()

# Función para agregar una misión manteniendo el orden de dificultad
def agregar_mision(nombre, dificultad):
    global misiones # La variable 'global' sirve para indicar que la variable 'misiones' es la misma que la definida fuera de la función
    nueva_mision = (nombre, dificultad)
    misiones.append(nueva_mision)  # Agregamos la misión
    misiones = deque(sorted(misiones, key=lambda m: m[1]))  # Reordenamos
    # key=lambda m: m[1] indica que se ordene por el segundo elemento de la tupla (la dificultad)

# Función para obtener la siguiente misión
def obtener_siguiente_mision():
    return misiones.popleft() if misiones else None

# Función para mostrar las misiones sin la dificultad
def mostrar_misiones():
    for mision in misiones:
        print(mision[0])

# Agregamos las misiones
agregar_mision("Rescatar al prisionero", 3)
agregar_mision("Recolectar suministros", 1)
agregar_mision("Defender la base", 2)

# Mostramos las misiones ordenadas
mostrar_misiones()



# Otra manera de hacerlo es con POO 
class Mision:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __lt__(self, other):
        return self.dificultad < other.dificultad

class ColaDeMisiones:
    def __init__(self):
        self.misiones = deque()

    def agregar_mision(self, mision):
        self.misiones.append(mision)
        self.misiones = deque(sorted(self.misiones))

    def obtener_siguiente_mision(self):
        if self.misiones:
            return self.misiones.popleft()
        else:
            return None

    def mostrar_misiones(self):
        for mision in self.misiones:
            print(mision.nombre)

# Ejemplo de uso
cola = ColaDeMisiones()
cola.agregar_mision(Mision("Rescatar al prisionero", 3))
cola.agregar_mision(Mision("Recolectar suministros", 1))
cola.agregar_mision(Mision("Defender la base", 2))

cola.mostrar_misiones()