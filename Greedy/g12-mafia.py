# Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. 
# Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales 
# no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos 
# por el control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un 
# rango de kilómetros 
# (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). 
# Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo 
# (es decir, no pueden solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje 
# sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. Ahora bien, esto es una mafia, 
# no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de 
# permisos otorgados (asegurándose de no otorgarle algún lugar a dos mafias diferentes). Implementar un 
# algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les 
# otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la 
# cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado. Justificar 
# por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de 
# la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

from tests import *

# CODIGO

INICIO = 0
FINALIZACION = 1
ES_NECESARIO_CREAR_ETIQUETA = -1
NUEVA_ETIQUETA_CON_1_ELEMENTO = 1

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


def obtener_set_optimo(set):
    set_ordenado = merge_sort(set)
    primer_horario = set_ordenado[0]
    tam_set = len(set)

    set_optimo = []
    set_optimo.append(primer_horario)

    finalizacion_por_etiqueta = [] # cada ultimo elemento de una etiqueta, se guarda aca, las posicion i es el valor de una etiqueta
    etiquetas = [] # se guarda el valor de la etiqueta de cada elemento vi (posicion en el vector finalizacion_etiqueta) 
    cant_curros_por_etiquetas = [] # cada posicion, es una etiqueta, donde se va ir guardando la cant de elemntos con esa misma


    for elemento_actual in set_ordenado:
        etiqueta_actual = obtener_etiqueta(elemento_actual, finalizacion_por_etiqueta)

        if etiqueta_actual == ES_NECESARIO_CREAR_ETIQUETA:
            finalizacion_por_etiqueta.append(elemento_actual[FINALIZACION])
            etiqueta_actual = len(finalizacion_por_etiqueta) - 1
            cant_curros_por_etiquetas.append(NUEVA_ETIQUETA_CON_1_ELEMENTO)
        else:
            cant_curros_por_etiquetas[etiqueta_actual] += 1
        etiquetas.append(etiqueta_actual)

    mejor_curro = 0
    for cant_curros_actual in cant_curros_por_etiquetas:
        if cant_curros_actual > mejor_curro:
            mejor_curro = cant_curros_actual

    for elemento in set_ordenado:
        set_optimo.append(elemento)

    return set_optimo


def obtener_etiqueta(elemento_actual, finalizacion_por_etiqueta):

    for pos_etiqueta, finalizacion_anterior in enumerate(finalizacion_por_etiqueta):

        if elemento_actual[FINALIZACION] > finalizacion_anterior:
            return pos_etiqueta
    return ES_NECESARIO_CREAR_ETIQUETA



    # se superpone? 
    # SI. excluyo etiqueta (aumento) y le asigno la etiqueta 
    # 

    pass


# pedidos: lista de tuplas con (km inicio, km fin)  [(5,10), (12,15)]
def asignar_mafias(pedidos):
    if len(pedidos) <= 1:
        return pedidos
    return obtener_set_optimo(pedidos)



# TESTS

kilometros_test = [ # [provistos, esperados]
    # [ [],                                                           [] ],
    [[(12, 15), (5, 10)],                                           [(5, 10), (12, 15)]],
    # [[(5, 10)],                                                     [(5, 10)]],
    # [[(1, 11), (10, 13), (12, 25)],                                 [(1, 11), (12, 25)]],
    # [[(1, 3), (2, 5), (4, 7), (5, 6), (6, 8), (8, 10), (9, 11)],    [(2, 5), (5, 6), (6, 8), (9, 11)]]
    # [[(2, 15), (3, 7), (1, 11), (6, 9), (10, 13), (5, 8), (12, 25), (17, 22), (16, 18), (14, 15), (14, 20)], horarios3],
]

ejecutar_tests(kilometros_test, asignar_mafias)