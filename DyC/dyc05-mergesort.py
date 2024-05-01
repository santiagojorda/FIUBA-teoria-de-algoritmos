# Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea de ordenamiento "por Merge Sort".
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

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
        
    







# TESTS

def ejecutar_tests(lista_tests, funcion):   
    exitos = 0
    fallos = 0
    for i, test in enumerate(lista_tests): 
        arr, esperado = test
        calculado = funcion(arr)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"Arreglo: {arr} \n", 
            f"Arreglo esperado:  {esperado} \n",
            f"Arreglo calculado: {calculado}\n")
        if calculado == esperado:
            print("")
            exitos = exitos + 1
        else:
            print("--------- FALLO\n")
            fallos = fallos + 1

    print(f"RESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")


# numero, raiz esperado
arr1 = [1, 2, 3, 4, 6, 5, 10, 7]
arr1_or = [1, 2, 3, 4, 5, 6, 7, 10]

arr2 = [0, 3, 1]
arr2_or = [0, 1, 3]

arr3 = []
arr3_or = []

arr4 = [1]
arr4_or = [1]

lista_tests = [
    [arr1, arr1_or],
    [arr2, arr2_or],
    [arr3, arr3_or],
    [arr4, arr4_or]
]
ejecutar_tests(lista_tests, merge_sort)