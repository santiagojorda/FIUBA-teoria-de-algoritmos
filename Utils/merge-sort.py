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