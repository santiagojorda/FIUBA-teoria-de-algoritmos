# Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: 
# estrictamente creciente hasta una determinada posición p, y estrictamente 
# decreciente a partir de ella (con 0 < p < N - 1). 
# Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2.

# Se pide:

#   1. Implementar un algoritmo de división y conquista de orden O(log n) que encuentre
#      la posición p del pico: func PosicionPico(v []int, ini, fin int) int. 
#      La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), 
#      y tiene como pre-condición que el arreglo tenga forma de pico.

#   2. Justificar el orden del algoritmo mediante el teorema maestro.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))".
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

def posicion_pico(arr, inicio, final):
    if inicio == final:
        return inicio

    medio = (inicio + final) // 2

    if arr[medio-1] < arr[medio] and arr[medio] > arr[medio+1]:
        return medio
    if arr[medio - 1] < arr[medio] and arr[medio] < arr[medio + 1]:
        return posicion_pico(arr, medio+1, final)
    if arr[medio - 1] > arr[medio] and arr[medio] > arr[medio + 1]:
        return posicion_pico(arr, inicio, medio)



# ANALISIS DE COMPLEJIDAD
# A T(n/B) + O(n^c)

# En este ejercicio aplico la busqueda binaria
# A es la cantidad de llamadas recursivas que tengo en mi algoritmo
# se puede ver que hay una ya que se llama en la linea 10 o en la linea 12, nunca juntas
# A = 1

# B es la proporcion a la que subdivido el arreglo en cada llamado recursivo
# Como estoy dividiendo a la mitad: T(n/2) 

# En el siguiente termino O(n^c) se hace referencia al costo de las operaciones restantes del algoritmo, tales como comparacion, asignacion, una divicion y retorno, siendo asi O(1) = O(n^C) => C = 0

# A = 1
# B = 2
# C = 0

# Quedando asi la expresion AT(n/B) + O(n^c) = 1T(n/2) + O(1)

# Aplicando el TEOREMA DE MAESTRO
# si log_B(A) = log_2(1) = 0 = C 
# => T(n) = O(n^C * log_B(n)) = O(log_2(n)) = O(log(n))

# Quedando asi el orden de complejidad del algoritmo: 
# T(n) = O(log(n))



# TESTS

def ejecutar_tests(lista_tests, funcion):    
    exitos = 0
    fallos = 0

    for i, test in enumerate(lista_tests): 
        arr, esperado = test
        calculado = posicion_pico(arr, 0, len(arr) - 1)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"arreglo: {arr} \n", 
            f"Posicion pico esperada: {esperado} \n",
            f"Posicion pico calculado: {calculado}")
        if calculado == esperado:
            print("")
            exitos = exitos + 1
        else:
            print("--------- FALLO\n")
            fallos = fallos + 1

    print(f"RESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")
    

arr1 = [1, 3, 1, 0, -2]
arr2 = [1, 2, 3, 1, 0, -2]
lista_tests = [
    [arr1, 1],
    [arr2, 2],
    
]
ejecutar_tests(lista_tests, posicion_pico)