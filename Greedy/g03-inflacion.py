# Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una
# era de inflación y los precios aumentan todo el tiempo. 
# El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). 
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos.
# Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra 
# siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy".
#  Por las características de la herramienta, no podemos verificarlo de forma automática,
# pero se busca que se implemente con dicha restricción

# ---------------------------

# Complejidad algoritmica
# 1- Los productos se ordenan por precio O(nlogn)
# 2- Se recorren todos los productos O(n)
# T(n) = O(nlogn) + O(n) = O(nlogn)

# Este algoritmo greedy se trata de uno optimo. 

# En resumen, el algoritmo greedy propuesto es optimo porque aprovecha la estructura del problema 
# (precios crecientes exponencialmente) para tomar decisiones locales optimas en cada paso / dia, 
# lo que garantiza que siempre encuentre el precio minimo al que podemos comprar todos los productos.

from tests import *

# CODIGO

def merge_sort(arr):
    tam = len(arr)

    if tam == 0:
        return arr

    final = tam - 1
    return dyc_merge_sort(arr, 0, final)

def dyc_merge_sort(arr, inicio, final):

    if inicio == final:
        return arr

    mitad = (inicio + final) // 2
    dyc_merge_sort(arr, inicio, mitad)
    dyc_merge_sort(arr, mitad+1, final)

    return merge(arr, inicio, mitad, final)

def merge(arr, inicio, mitad, final):

    i = inicio
    j = mitad + 1

    aux = []

    while i <= mitad and j <= final:
        if arr[i] > arr[j]:
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

def precios_inflacion(R):

    tam = len(R)

    if tam == 0:
        return 0

    productos_ordenados = merge_sort(R)
    j = 0
    precio_min = 0

    while j != tam: 

        precio_min += productos_ordenados[tam - 1 - j] ** (j + 1)

        j += 1


    return precio_min




# TESTS 

tests = [
    [[10], 10],
    [[], 0],
    # [[5, 20, 10], ],
]

ejecutar_tests(tests, precios_inflacion)