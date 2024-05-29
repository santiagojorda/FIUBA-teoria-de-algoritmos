# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de 
# la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3,
# y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

# Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz 
# cuadrada, ni de forma exacta ni aproximada.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". 
# Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca 
# que se implemente con dicha restricción

from tests import *

# CODIGO

def parte_entera_raiz(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    mitad = n // 2
    return dividir_y_conquistar(n, mitad, n)

def dividir_y_conquistar(n, raiz, cota_sup, cota_inf = None):
    cuadrado = raiz**2
    cuadrado_del_siguiente = (raiz + 1)**2

    if cuadrado == n or cuadrado_del_siguiente > n and cuadrado < n:
        return raiz

    if cuadrado > n: 
        mitad = raiz // 2
        if cota_inf != None and mitad < cota_inf:
            mitad = (cota_inf + raiz) // 2
            return dividir_y_conquistar(n, mitad, raiz, cota_inf)
        return dividir_y_conquistar(n, mitad, raiz)
     
    else: 
        cota_inf = raiz
        mitad = (cota_inf + cota_sup) // 2
        return dividir_y_conquistar(n, mitad, cota_sup, cota_inf)



# TESTS

# numero, raiz esperado
lista_tests = [
    [1, 1],
    [0, 0],
    [3, 1],
    [25,5],
    [9, 3],
    [10, 3],
    [37, 6],
    [170, 13],
    [6564378, 2562],
    [99, 9],
]
ejecutar_tests(lista_tests, parte_entera_raiz)