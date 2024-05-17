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

from grafo import *


# ---

def no_adyacentes(grafo, n):
    vertices = grafo.obtener_vertices()
    if len(vertices) <= 1:
        return False
    
    visitados = []  # contiene vertices
    colores = []    # contiene numeros de colores, correspondiente a cada elemento de visitados
    return coloreo(grafo, vertices, visitados, colores, n)


def coloreo(grafo, vertices, vi, visitados, colores, n):

    if len(visitados) == len(vertices):
        if()


    pass




    # vertices = grafo.obtener_vertices()
    # solucion = []
    # visitados = []

    # solucion_parcial
    # for vi in vertices: 
    #     if backtracking(grafo, vertices, solucion, visitados, vi, n):
    #         pass

    # if solucion != []:
    #     return solucion
    # return None




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
