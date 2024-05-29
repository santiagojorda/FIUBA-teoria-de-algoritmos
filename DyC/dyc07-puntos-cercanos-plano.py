# Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre
# más cercana, por división y conquista, con un orden de complejidad mejor que O(n^2).
# Justificar el orden del algoritmo mediante el teorema maestro.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, 
# en tiempo mejor que O(n^2)". Por las características de la herramienta, no podemos verificarlo 
# de forma automática, pero se busca que se implemente con dicha restricción

# Supongo que ningun par de puntos comparte la coordenada x o y   

# MERGE SORT UTILIZANDO EN EL EJERICICIO 5 DE DYC
# ORDENO Y

from tests import *

# AUXILIAR

def merge_sort_x(arr):
    tam = len(arr)

    if tam == 0:
        return arr

    final = tam - 1
    return dyc_merge_sort_x(arr, 0, final)

def dyc_merge_sort_x(arr, inicio, final):

    if inicio == final:
        return arr

    mitad = (inicio + final) // 2
    dyc_merge_sort_x(arr, inicio, mitad)
    dyc_merge_sort_x(arr, mitad+1, final)

    return merge_x(arr, inicio, mitad, final)

def merge_x(arr, inicio, mitad, final):

    i = inicio
    j = mitad + 1

    aux = []

    while i <= mitad and j <= final:
        if arr[i].x > arr[j].x:
            aux.append(arr[j])
            j = j+1
        else:
            aux.append(arr[i])
            i = i+1
        
    while i <= mitad:
        aux.append(arr[i])
        i = i+1
    
    while j <= final:
        aux.append(arr[j])
        j = j+1

    for indice, val in enumerate(aux):
        arr[inicio + indice] = val
    return arr


# ORDENO X
def merge_sort_y(arr):
    tam = len(arr)

    if tam == 0:
        return arr

    final = tam - 1
    return dyc_merge_sort_y(arr, 0, final)

def dyc_merge_sort_y(arr, inicio, final):

    if inicio == final:
        return arr

    mitad = (inicio + final) // 2
    dyc_merge_sort_y(arr, inicio, mitad)
    dyc_merge_sort_y(arr, mitad+1, final)

    return merge_y(arr, inicio, mitad, final)

def merge_y(arr, inicio, mitad, final):

    i = inicio
    j = mitad + 1

    aux = []

    while i <= mitad and j <= final:
        if arr[i].y > arr[j].y:
            aux.append(arr[j])
            j = j+1
        else:
            aux.append(arr[i])
            i = i+1
        
    while i <= mitad:
        aux.append(arr[i])
        i = i+1
    
    while j <= final:
        aux.append(arr[j])
        j = j+1

    for indice, val in enumerate(aux):
        arr[inicio + indice] = val
    return arr

# CODIGO

def puntos_mas_cercanos(puntos):

    px = merge_sort_x(puntos)
    print(px)
    py = merge_sort_y(puntos)
    print(py)

    
    return [(0,0), (0,0)]


# TESTS

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

# numero, raiz esperado
p0 = Punto(0,13)
p2 = Punto(24, 22)
p1 = Punto(1, 1)
p3 = Punto(5, 2)
p4 = Punto(12, 10)
p5 = Punto(10, 3)
puntos_tests = [
    [[p0, p2, p1, p3, p4, p5], [p1, p3]]
    
]

ejecutar_tests(puntos_tests, puntos_mas_cercanos)