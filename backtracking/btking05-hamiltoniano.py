
# NOTAS
# Recorrer todo el grafo pasando 1 vez por cada vertice
# la idea es evitar visitar vertices que ya recorri
# al hacer esto, hago un dfs?

from grafo import *

def obtener_camino(grafo):
    vertices = grafo.obtener_vertices()
    if len(vertices) == 0:
        return None
    for vi in vertices:
        camino = []
        if camino_hamiltoniano_dfs(grafo, vertices, vi, camino):
            return camino
    return None

def camino_hamiltoniano_dfs(grafo, vertices, v_actual, camino):
    camino.append(v_actual)

    if len(camino) == len(vertices):
        return True
    
    adyaentes = grafo.adyacentes(v_actual)
    for ady in adyaentes:
        if ady not in camino:
            if camino_hamiltoniano_dfs(grafo, vertices, ady, camino):
                return True
    camino.remove(v_actual)
    return False 


# --- TESTS

grafo = Grafo_no_dirigido_sin_peso()

grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_arista("A", "B")
grafo.agregar_arista("C", "B")
print(obtener_camino(grafo))