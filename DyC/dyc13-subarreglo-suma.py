# Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), 
# encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. 
# Indicar y justificar la complejidad del algoritmo. Ejemplos:

# [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
# [5, 3, -5, 4, -1] ->  [5, 3]
# [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
# [5, -4, 2, 4] -> [5, -4, 2, 4]

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista".
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

from tests import *

# CODIGO

def max_subarray(arr):
    tam = len(arr)
    if tam <= 1:
        return arr
    
    inicio = 0
    final = tam - 1
    
    i_arr, f_arr, suma = dividir_y_obtener_intervalo_max(arr, inicio, final)
    return arr[i_arr:f_arr + 1] 

def sumar_medio(arr, inicio, mitad, final):

    sumaIzquierda = sumaMaxima = float('-inf')
    max_right = mitad
    max_left = mitad
    for i in range(mitad, inicio - 1, -1):
        sumaIzquierda += arr[i]
        sumaMaxima = max(sumaMaxima, sumaIzquierda)
        if sumaMaxima > sumaIzquierda:
            left_sum = sumaIzquierda
            max_left = i
    
    sumaDerecha = float('-inf')
    for i in range(mitad + 1, final + 1):
        sumaDerecha += arr[i]
        sumaMaxima = max(sumaMaxima, sumaDerecha)
        if sumaMaxima > sumaDerecha:
            right_sum = sumaDerecha
            max_right = i
    
    return max_left, max_right, sumaMaxima

def dividir_y_obtener_intervalo_max(arr, inicio, final):

    if inicio == final:
        return inicio, final, arr[inicio]

    mitad = (inicio + final) // 2

    i_izq, f_izq, suma_izq = dividir_y_obtener_intervalo_max(arr, inicio, mitad)
    i_der, f_der, suma_der = dividir_y_obtener_intervalo_max(arr, mitad + 1, final)
    i_medio, f_medio, suma_medio = sumar_medio(arr, inicio, mitad, final)

    if suma_izq >= suma_der and suma_izq >= suma_medio:
        return i_izq, f_izq, suma_izq
    elif suma_der >= suma_izq and suma_der >= suma_medio:
        return i_der, f_der, suma_der
    else:
        return i_medio, f_medio, suma_medio


# def son_ambos_negativos(num1, num2):
#     return num1 < 0 and num2 < 0


# def son_continuos(num_menor, num_mayor):
#     return num_mayor == num_menor + 1 


# def dividir_y_obtener_intervalo_max(arr, inicio, final):

#     if inicio == final:
#         return inicio, final, arr[inicio]
    
#     mitad = (inicio + final) // 2

#     i_izq, f_izq, suma_izq = dividir_y_obtener_intervalo_max(arr, inicio, mitad)
#     i_der, f_der, suma_der = dividir_y_obtener_intervalo_max(arr, mitad + 1, final)
    
#     if son_ambos_negativos(suma_izq, suma_der):
#         if suma_izq > suma_der:
#             return i_izq, f_izq, suma_izq
#         else: 
#             return i_der, f_der, suma_der

#     else: 
#         if son_continuos(f_izq, i_der):

#             if suma_izq > 0 and suma_der < 0:
#                 return i_izq, f_izq, suma_izq
            
#             elif suma_izq < 0 and suma_der > 0:
#                 return i_der, f_der, suma_der
            
#             return i_izq, f_der, (suma_izq + suma_der)

#         else: 

#             suma_der_aux = 0
#             suma_izq_aux = 0
#             i_der_aux = i_der
#             f_izq_aux = f_izq
#             suma_medio = 0

#             for i in range(f_izq + 1, i_der):
#                 suma_der_aux += arr[i]
#                 suma_medio += arr[i]
#                 if arr[i] < 0:
#                     i_der_aux = i
#                     suma_der_aux = 0
#                     suma_izq_aux = 0
#                 else:
#                     f_izq_aux = i
#                     suma_izq_aux += arr[i]


#             if suma_izq + suma_medio > 0 and suma_der + suma_medio > 0:
#                 return i_izq, f_der, (suma_izq + suma_medio + suma_der)
            
#             if f_izq != mitad:
#                 i_der = i_der_aux + 1
#                 suma_der += suma_der_aux
            
#             if i_der != mitad + 1:
#                 f_izq = f_izq_aux
#                 suma_izq += suma_izq_aux

#             if suma_der > suma_izq:
#                 return i_der, f_der, suma_der 
#             else:
#                 return i_izq, f_izq, suma_izq




    


# --- TESTS 


tests = [  
    [ [],                                     [] ],
    [ [5],                                    [5] ],
    [ [-1],                                   [-1] ],
    [ [5, 4],                                 [5, 4] ],
    [ [-5, -4],                               [-4] ],
    # [ [5, 3, 2, 4, -1],                       [5, 3, 2, 4] ],
    # [ [-5, -3, -5],                           [-3] ],
    # [ [5, 3, -5, 6, -1],                      [5, 3, -5, 6] ],
    # [ [5, 3, -5],                             [5, 3] ],
    # [ [-5, 3, -5],                            [3] ],
    # [ [-5, 3, 5],                             [3, 5] ],
    # [ [5, 3, -5, 4, -1],                      [5, 3] ],
    # [ [5, 3, -5, -1, 4, -1],                  [5, 3] ],
    # [ [5, 3, -5, -1, 9, -1],                  [5, 3, -5, -1, 9] ],
    # [ [5, 3, 5, -1, 9, -1],                   [5, 3, 5, -1, 9] ],
    # [ [7, -10, 6, 2, -5, 6, -6, 7],           [6, 2, -5, 6, -6, 7] ],
    [ [-3, 4, -1, 2, 1, 2, -5, 1, 2, 1],      [4, -1, 2, 1, 2] ],
    # [ [2, -5, 1, 2, 1],                       [1, 2, 1] ],
    # [ [2, 1, -4, 5, 1, -5, 2],                [5, 1] ],
    # [ [-2, -5, 6, -2, -3, 1, 5, -6],          [6, -2, -3, 1, 5]]
]


ejecutar_tests(tests, max_subarray)