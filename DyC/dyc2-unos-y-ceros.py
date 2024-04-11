# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros).
# Se pide una función de orden O(log(n)) que encuentre el índice del primer 0. 
# Si no hay ningún 0 (solo hay unos), debe devolver -1.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en O(log(n))". 
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

CERO = 0
NO_HAY_CERO = -1

def indice_primer_cero(arr):
    inicio = 0
    final = len(arr) - 1
    return dividr_y_obtener_indice_primer_cero(arr, inicio, final)

def obtener_indice_primer_cero_del_par(arr, izq, der):
    if arr[izq] == CERO:
        return izq
    return der
    

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



# CASO 1
arr = [1, 1, 1, 0, 0, 0, 0, 0]
indice = indice_primer_cero(arr)
print("\n",
      "- CASO 1\n", 
      f"{arr} \n", 
      f"Indice esperado: 3\n",
      f"Indice calculado: {indice} \n\n")

# CASO 2
arr = [1, 1, 0, 0, 0, 0]
indice = indice_primer_cero(arr)
print("\n",
      "- CASO 2\n", 
      f"{arr} \n", 
      f"Indice esperado: 2\n",
      f"Indice calculado: {indice} \n\n")

# CASO 3
arr = [1, 1, 1, 1, 1]
indice = indice_primer_cero(arr)
print("\n",
      "- CASO 3\n", 
      f"{arr} \n", 
      f"Indice esperado: {NO_HAY_CERO} \n",
      f"Indice calculado: {indice} \n\n")