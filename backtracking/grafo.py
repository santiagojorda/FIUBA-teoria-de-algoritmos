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
