# Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos
# y casi ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento 
# fuera de lugar. Indicar y justificar el orden.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". 
# Por las características de la herramienta, no podemos verificarlo de forma automática,
# pero se busca que se implemente con dicha restricción

def elemento_desordenado(arr):
    inicio = 0
    final = len(arr) - 1
    return dividir_y_encontrar_desubicado(arr, inicio, final)


def obtener_desubicado_2_elementos(izq, der):
  if izq > der:
    return izq
  return None

def dividir_y_encontrar_desubicado(arr, inicio, final):

  if inicio == final:
    return None

  if final == inicio + 1:
    return obtener_desubicado_2_elementos(arr[inicio], arr[final])

  medio = (inicio + final) // 2

  if arr[medio - 1] < arr[medio] and arr[medio] < arr[medio + 1]:
    desubicado_izq = dividir_y_encontrar_desubicado(arr, inicio, medio)
    desubicado_der = dividir_y_encontrar_desubicado(arr, medio + 1, final)

    if desubicado_izq != None:
      return desubicado_izq
    if desubicado_der != None:
      return desubicado_der
    return None 


  else:
    if arr[medio - 1] > arr[medio]:
      return arr[medio - 1]
    return arr[medio]



# CASO 1
arr = [2, 4, 6, 8, 10, 9, 12, 14]
elemento = elemento_desordenado(arr)
print("\n",
      "- CASO 1\n", 
      f"{arr} \n", 
      f"Elemento fuera de lugar esperado: 10 \n",
      f"Elemento fuera de lugar calculado: {elemento} \n\n")


# CASO 2
arr = [2, 5, 3]
elemento = elemento_desordenado(arr)
print("\n",
      "- CASO 2\n", 
      f"{arr} \n", 
      f"Elemento fuera de lugar esperado: 5 \n",
      f"Elemento fuera de lugar calculado: {elemento} \n\n")