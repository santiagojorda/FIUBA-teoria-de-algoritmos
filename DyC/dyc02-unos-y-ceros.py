# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros).
# Se pide una función de orden O(log(n)) que encuentre el índice del primer 0. 
# Si no hay ningún 0 (solo hay unos), debe devolver -1.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en O(log(n))". 
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

from tests import *

# CODIGO

CERO = 0
NO_HAY_CERO = -1

def indice_primer_cero(arr):
    inicio = 0
    final = len(arr) - 1
    return dividr_y_obtener_indice_primer_cero(arr, inicio, final)

def obtener_indice_primer_cero_del_par(arr, izq, der):
    if arr[izq] == CERO:
        return izq
    if arr[der] == CERO:
        return der
    return NO_HAY_CERO
    

def dividr_y_obtener_indice_primer_cero(arr, inicio, final):

    if inicio == final:
        if arr[inicio] == CERO:
            return inicio
        return NO_HAY_CERO

    if final == inicio + 1:
        return obtener_indice_primer_cero_del_par(arr, inicio, final)

    medio = (inicio + final) // 2

    if arr[medio] == CERO:
        return dividr_y_obtener_indice_primer_cero(arr, inicio, medio)
    else:
        return dividr_y_obtener_indice_primer_cero(arr, medio+1, final)


# TESTS

arr_3 = [1, 1, 1, 0, 0, 0, 0, 0]
arr_2 = [1, 1, 0, 0, 0, 0]
arr_sin_ceros = [1, 1, 1, 1, 1]
lista_tests = [
    [arr_3, 3],
    [arr_2, 2],
    [arr_sin_ceros, NO_HAY_CERO]
]

ejecutar_tests(lista_tests, indice_primer_cero)
