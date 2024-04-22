# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
# Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, 
# representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin,
# e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. 
# Indicar y justificar la complejidad del algoritmo implementado.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy".
# Por las características de la herramienta, no podemos verificarlo de forma automática,
# pero se busca que se implemente con dicha restricción


INICIO = 0
FINALIZACION = 1

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
        if arr[i][FINALIZACION] > arr[j][FINALIZACION]:
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

def obtener_set_optimo(horarios):
    horarios_ordenados = merge_sort(horarios)

    primer_horario = horarios_ordenados[0]
    finalizacion = primer_horario[FINALIZACION]
    
    set_optimo = []
    set_optimo.append(primer_horario)

    for horario in horarios_ordenados[1:]:
        if horario[INICIO] >= finalizacion:
            set_optimo.append(horario)
            finalizacion = horario[FINALIZACION]

    return set_optimo

def charlas(horarios):
    if len(horarios) <= 1:
        return horarios
    return obtener_set_optimo(horarios)


# COMPLEJIDAD ALGORITMICA
# 1- Merge sort: O(nlogn)
# 2- Recorre lista ordenada O(n)
# Sumando T(n) = O(nlogn) + O(n) = O(nlogn)



# TESTS 

def ejecutar_tests(lista_tests, funcion):    
    exitos = 0
    fallos = 0

    for i, test in enumerate(lista_tests): 
        horarios, esperado = test
        calculado = funcion(horarios)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"Horarios: {horarios} \n", 
            f"Set esperado: {esperado} \n",
            f"Set calculada: {calculado}")
        if calculado == esperado:
            exitos = exitos + 1
            print("--------- EXITO\n")
        else:
            print("--------- FALLO\n")
            fallos = fallos + 1

    print(f"RESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")

# numero, raiz esperado
horarios1 = [(5, 10), (12, 15)]
horarios2 = [(2, 15), (3, 7), (1, 11), (6, 9), (10, 13), (5, 8), (12, 25), (17, 22), (16, 18), (14, 15), (14, 20)]
horarios3 = [(5, 10)]

horarios_test = [
    [ [], [] ],
    [horarios3, horarios3],
    [horarios1, horarios1],
]

ejecutar_tests(horarios_test, charlas)