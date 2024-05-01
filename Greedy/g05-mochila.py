# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, 
# y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin 
# exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos 
# de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 
# Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado 
# encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? 
# Justificar

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

# ------

# Complejidad algoritmica
# 1- Ordeno O(nlogn)
# 2- Recorro la lista O(n)
# T(n) = O(nlogn)

VALOR = 0
PESO = 1

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
        if arr[i][VALOR] > arr[j][VALOR]:
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

def mochila(elementos, W):
    if elementos == []:
        return []
    
    tam = len(elementos)
    elementos_ordenados = merge_sort(elementos)
    espacio_disponible = W
    i = tam - 1
    elementos_guardados = []
    while espacio_disponible > 0 and i >= 0:
        espacio_parcial = espacio_disponible - elementos_ordenados[i][PESO]
        if espacio_parcial >= 0:
            espacio_disponible = espacio_parcial
            elementos_guardados.append(elementos_ordenados[i])
        i -= 1

    return elementos_guardados




# TESTS 

def ejecutar_tests(lista_tests, funcion):    
    exitos = 0
    fallos = 0

    for i, test in enumerate(lista_tests): 
        valores, peso_maximo, esperado = test
        calculado = funcion(valores, peso_maximo)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"(Valor, Peso): {valores} \n", 
            f"Peso maximo: {peso_maximo} \n", 
            f"Elementos guardados max ganancia esperados: {esperado} \n",
            f"Elementos guardados para max ganancia calculados: {calculado}")
        if calculado == esperado:
            exitos = exitos + 1
            print("--------- EXITO\n")
        else:
            print("--------- FALLO\n")
            fallos = fallos + 1

    print(f"RESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")


tests = [
    [ [], 10, [] ],
    [ [(5, 10)], 10, [(5,10)] ],
    [ [(5, 5), (3, 3), (7, 7)], 10, [(7,7), (3,3)] ]
]

ejecutar_tests(tests, mochila)