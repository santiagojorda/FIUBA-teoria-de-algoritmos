# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un 
# conjunto de vértices que representen un máximo Independent Set del mismo.

MENSAJE_NO_EXISTE_VERTICES = 'Error: uno o ambos vértices no existen en el grafo'
MENSAJE_VERTICES_NO_ADYACENTES = 'Error: los vertices no son adyacentes'

class Grafo_no_dirigido_sin_peso:
    def __init__(self):
        self.vertices = {}  # Diccionario para almacenar los vértices y sus conexiones

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []  # Inicializamos la lista de conexiones para el nuevo vértice

    def estan_unidos(self, vertice_origen, vertice_destino):
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            if vertice_destino in self.vertices[vertice_origen]:
              return True
            return False
        else:
            print(MENSAJE_NO_EXISTE_VERTICES)
            return False
        
    def agregar_arista(self, vertice_origen, vertice_destino):
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            self.vertices[vertice_origen].append(vertice_destino) # Agregamos la conexión de origen a destino
            self.vertices[vertice_destino].append(vertice_origen) # Agregamos la conexión de origen a destino
        else:
            print(MENSAJE_NO_EXISTE_VERTICES)

    def borrar_arista(self, vertice_origen, vertice_destino):
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            if vertice_origen in self.adyacentes(vertice_destino):
                self.vertices[vertice_origen].remove(vertice_destino) # Agregamos la conexión de origen a destino
                self.vertices[vertice_destino].remove(vertice_origen) # Agregamos la conexión de origen a destino
            else:
                print(MENSAJE_VERTICES_NO_ADYACENTES)
        else: 
            print(MENSAJE_NO_EXISTE_VERTICES)

    def adyacentes(self, vertice_origen):
        return list(self.vertices[vertice_origen])
    
    def imprimir(self):
        for vertice, conexiones in self.vertices.items():
            print(f"{vertice}: {conexiones}")

# --- CODE

def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    tam = len(vertices)
    
    if tam <= 1:
        print('grafo tiene cero o una arista')
        return grafo

    colores = []
    solucion = []

    for vi, v in enumerate(vertices):
        coloreo(grafo, vertices, colores, solucion, vi, 1)

    return solucion

def coloreo(grafo, vertices, colores, solucion, vi, n):
    if vi >= len(vertices):
        return colores

    for color in range(1, n+1):
        colores.append(color)

        if compatible(grafo, vertices, colores, vi, n):
            if coloreo(grafo, vertices, colores, solucion, vi+1, n):
                return True
        colores.pop()
    return False
    
def compatible(grafo, vertices, colores, vi, n):
    v_actual = vertices[vi]
    adyacentes = grafo.adyacentes(v_actual)

    for ady in adyacentes:
        ady_index = vertices.index(ady)
        
        if ady_index < vi and colores[ady_index] == colores[vi]:
            return False
    return True

# COMPLEJIDAD BACKTRAKING
# POR FUERZA BRUTA ES O(2^N)
# LA PODA LO HACE MEJOR, PERO LA COMPLEJIDAD SIGUE SIENDO LA MISMA
# 

# --- TESTS

grafo = Grafo_no_dirigido_sin_peso()

grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B")
grafo.agregar_arista("B", "C")


print(independent_set(grafo))