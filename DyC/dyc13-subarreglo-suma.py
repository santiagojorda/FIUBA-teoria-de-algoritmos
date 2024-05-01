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

# --- EJERCICIO

def max_subarray(arr):
    tam = len(arr)
    if tam <= 1:
        return arr
    
    inicio = 0
    final = tam - 1
    
    i_arr, f_arr, suma = dividir_y_obtener_intervalo_max(arr, inicio, final)
    return arr[i_arr:f_arr + 1] 


def son_ambos_negativos(num1, num2):
    return num1 < 0 and num2 < 0


def son_continuos(num_menor, num_mayor):
    return num_mayor == num_menor + 1 


def dividir_y_obtener_intervalo_max(arr, inicio, final):

    if inicio == final:
        return inicio, final, arr[inicio]
    
    mitad = (inicio + final) // 2

    i_izq, f_izq, suma_izq = dividir_y_obtener_intervalo_max(arr, inicio, mitad)
    i_der, f_der, suma_der = dividir_y_obtener_intervalo_max(arr, mitad + 1, final)
    
    if son_ambos_negativos(suma_izq, suma_der):
        if suma_izq > suma_der:
            return i_izq, f_izq, suma_izq
        else: 
            return i_der, f_der, suma_der

    else: 
        if son_continuos(f_izq, i_der):

            if suma_izq > 0 and suma_der < 0:
                return i_izq, f_izq, suma_izq
            
            elif suma_izq < 0 and suma_der > 0:
                return i_der, f_der, suma_der
            
            return i_izq, f_der, (suma_izq + suma_der)

        else: 
            suma_mitad = 0
            A_IZQ = arr[i_izq:f_izq + 1]
            A_DER = arr[i_der:f_der + 1]
            for i in range(f_izq + 1, i_der):
                suma_mitad += arr[i]

            if suma_izq + suma_mitad > 0 and suma_mitad + suma_der > 0:
                return i_izq, f_der, (suma_izq + suma_mitad + suma_der)  
            
            elif suma_izq > suma_der:
                return i_izq, f_izq, suma_izq
            else: 
                return i_der, f_der, suma_der



    


# --- TESTS 

def ejecutar_tests(lista_tests, funcion):    
    exitos = 0
    fallos = 0

    for i, test in enumerate(lista_tests): 
        datos_iniciales, esperado = test
        calculado = funcion(datos_iniciales)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"Datos iniciales: {datos_iniciales} \n", 
            f"Esperado: {esperado} \n",
            f"Calculado: {calculado}")
        if calculado == esperado:
            exitos = exitos + 1
            print("--------- EXITO\n")
        else:
            print("--------- FALLO\n")
            fallos = fallos + 1

    print(f"\nRESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")


tests = [   
    # [ [5, 3, 2, 4, -1],                       [5, 3, 2, 4] ],
    # [ [-5, -3, -5],                           [-3] ],
    # [ [5, 3, -5, 6, -1],                      [5, 3, -5, 6] ],
    # [ [5],                                    [5] ],
    # [ [-1],                                   [-1] ],
    # [ [5, 4],                                 [5, 4] ],
    # [ [-5, -4],                               [-4] ],
    # [ [5, 3, -5],                             [5, 3] ],
    # [ [-5, 3, -5],                            [3] ],
    # [ [-5, 3, 5],                             [3, 5] ],
    # [ [],                                     [] ],
    # [ [5, 3, -5, 4, -1],                      [5, 3] ],
    # [ [5, 3, -5, -1, 4, -1],                  [5, 3] ],
    # [ [5, 3, -5, -1, 9, -1],                  [5, 3, -5, -1, 9] ],
    # [ [5, 3, 5, -1, 9, -1],                   [5, 3, 5, -1, 9] ],
    # [ [-3, 4, -1, 2, 1, 2, -5, 1, 2, 1],      [4, -1, 2, 1, 2] ],
    [ [2, -5, 1, 2, 1],                       [1, 2, 1] ],
]


ejecutar_tests(tests, max_subarray)