# Implementar por backtracking un algoritmo que, dado un grafo no dirigido 
# y un numero n menor a #V, devuelva si es posible obtener un subconjunto 
# de n vertices tal que ningun par de vertices sea adyacente entre si.

# Métodos del grafo:

#     Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
#     agregar_vertice(self, v)
#     borrar_vertice(self, v)
#     agregar_arista(self, v, w, peso = 1)
#         el resultado será v <--> w
#     borrar_arista(self, v, w)
#     estan_unidos(self, v, w)
#     peso_arista(self, v, w)
#     obtener_vertices(self)
#         Devuelve una lista con todos los vértices del grafo
#     vertice_aleatorio(self)
#     adyacentes(self, v)
#     str

# ---

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


# ---

def no_adyacentes(grafo, n):

    vertices = grafo.obtener_vertices()
    solucion = []
    visitados = []

    solucion_parcial
    for vi in vertices: 
        if backtracking(grafo, vertices, solucion, visitados, vi, n):
            pass

    if solucion != []:
        return solucion
    return None




# def no_adyacentes(grafo, n):
    
#     vertices = grafo.obtener_vertices()

#     solucion = []
#     visitados = []

#     for vi in vertices:
#         if backtraking(grafo, vertices, solucion, visitados, vi, n):
#             return solucion
#     return None

# def compatible(solucion, visitados, adyacentes):
#     for ady in adyacentes:
#         if ady in visitados and ady in solucion:
#             return False
#     return True

# def backtraking(grafo, vertices, solucion, visitados, vi, n):
    
#     visitados.append(vi)
#     solucion.append(vi)
   
#     adyacentes = grafo.adyacentes(vi)
#     if not compatible(solucion, visitados, adyacentes):
#         solucion.pop()
#     else:
#         if len(solucion) == n and len(visitados) <= len(vertices):
#             return True

#     for ady in adyacentes:
#         if ady not in visitados:
#             if backtraking(grafo, vertices, solucion, visitados, ady, n):
#                 return True
#             # visitados.pop()
#     return False


# --


grafo = Grafo_no_dirigido_sin_peso()

# grafo.agregar_vertice("A")
# grafo.agregar_vertice("B")
# grafo.agregar_vertice("C")
# grafo.agregar_arista("A","B")
# grafo.agregar_arista("B","C")
# print(no_adyacentes(grafo, 2))

print('CONECTADOS')
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("A", "D")
print(no_adyacentes(grafo, 3), "\n")

# print('NO CONECTADOS')
# grafo = Grafo_no_dirigido_sin_peso()
# grafo.agregar_vertice("A")
# grafo.agregar_vertice("B")
# grafo.agregar_vertice("C")
# grafo.agregar_vertice("D")
# print(no_adyacentes(grafo, 4))
