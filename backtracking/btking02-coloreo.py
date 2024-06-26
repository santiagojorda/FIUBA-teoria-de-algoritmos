# Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, 
# indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos 
# vértices adyacentes con el mismo color.

# --- 

from grafo import *

# ---

# def colorear(grafo, n):
#     vertices = grafo.obtener_vertices()
#     tam = len(vertices)
    
#     if tam == 0:
#         return True

#     colores = []
#     vi = 0

#     if coloreo(grafo, vertices, colores, vi, n):
#         return True
#     return False

# def compatible(grafo, vertices, colores, vi, n):
#     v_actual = vertices[vi]
#     adyacentes = grafo.adyacentes(v_actual)

#     for ady in adyacentes:
#         ady_index = vertices.index(ady)
        
#         if ady_index < vi and colores[ady_index] == colores[vi]:
#             return False
#     return True

# def coloreo(grafo, vertices, colores, vi, n):
#     if vi >= len(vertices):
#         return True

#     for color in range(1, n+1):
#         colores.append(color)

#         if compatible(grafo, vertices, colores, vi, n):
#             if coloreo(grafo, vertices, colores, vi+1, n):
#                 return True
#         colores.pop()
#     return False
    





# def camino_hamiltoniano_dfs(grafo, v, visitados, camino, n):
#     visitados.append(v)
#     if len(camino) == n or len(visitados) == len(grafo.obtener_vertices()):
#         return True
#     camino.append(v)
    
#     for w in grafo.adyacentes(v):
#         if w not in visitados:
#             if camino_hamiltoniano_dfs(grafo, w, visitados, camino, n):
#                 return True

#     visitados.remove(v)
#     camino.remove(v)
#     return False

# def colorear(grafo, n): 
#     vertices = grafo.obtener_vertices()
#     visitados = []
#     camino = []
    
#     if n > len(vertices):
#         return False

#     for v in vertices:
#         if camino_hamiltoniano_dfs(grafo, v, visitados, camino, n):
#             return True
#     return False


grafo = Grafo_no_dirigido_sin_peso()
# grafo.agregar_vertice("A")
# grafo.agregar_vertice("B")
# grafo.agregar_vertice("C")
# grafo.agregar_vertice("D")
# grafo.agregar_vertice("E")
# grafo.agregar_vertice("F")
# grafo.agregar_vertice("G")
# grafo.agregar_vertice("H")

# grafo.agregar_arista("A","B")
# grafo.agregar_arista("B","C")
# grafo.agregar_arista("B","F")
# grafo.agregar_arista("C","D")
# grafo.agregar_arista("D","E")
# grafo.agregar_arista("D","F")
# grafo.agregar_arista("F","G")
# grafo.agregar_arista("E","H")
# grafo.agregar_arista("G","H")
# print(grafo.estan_unidos("A","B"))
# grafo.imprimir()
# print(grafo.adyacentes("B"))
# print(grafo.obtener_vertices())
# print(no_adyacentes(grafo, 3))
# for i in range (0, 10):
#     print(colorear(grafo, i))



# grafo2 = Grafo_no_dirigido_sin_peso()
# grafo2.agregar_vertice("A")
# grafo2.agregar_vertice("B")
# grafo2.agregar_vertice("C")
# grafo2.agregar_arista("A", "B")
# grafo2.agregar_arista("C", "B")
# grafo2.agregar_arista("C", "A")
 
# print(f"grafo no bipartito n=2 -> False : {colorear(grafo2, 2)}")
# print(f"grafo no bipartito n=3 -> True  : {colorear(grafo2, 3)}")

# grafo3 = Grafo_no_dirigido_sin_peso()
# grafo3.agregar_vertice("A")
# grafo3.agregar_vertice("B")
# grafo3.agregar_vertice("C")
# grafo3.agregar_arista("A", "B")
# grafo3.agregar_arista("C", "B")
# grafo3.agregar_arista("C", "A")
 
# print(f"grafo no bipartito: ${colorear(grafo3, 2)}")

# grafoVacio = Grafo_no_dirigido_sin_peso()
# print(f"grafo vacio n=3 -> True  : {colorear(grafoVacio, 3)}")

grafo4 = Grafo_no_dirigido_sin_peso()
grafo4.agregar_vertice("A")
grafo4.agregar_vertice("B")
grafo4.agregar_vertice("C")
grafo4.agregar_vertice("D")
grafo4.agregar_arista("A", "B")
grafo4.agregar_arista("C", "B")
grafo4.agregar_arista("C", "D")
grafo4.agregar_arista("A", "D")
grafo4.agregar_arista("A", "C")
grafo4.agregar_arista("D", "B")

print(f"grafo no coloreable con n=3 -> False  : {colorear(grafo4, 3)}")
