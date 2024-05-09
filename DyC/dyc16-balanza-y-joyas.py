# Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something,
# que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron
# en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los
# refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que 
# no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya 
# verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera 
# va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. Cuenta con una balanza 
# de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

# En el ejemplo de código inicial de la actividad mostramos un llamado de ejemplo a la función balanza, 
# a la que se le deben pasar los dos conjuntos de joyas a verificar. La cantidad de joyas en cada conjunto 
# debe ser la misma, para que el resultado de la balanza de platillos nos dé información.
# Si los dos platillos pesan lo mismo, balanza devuelve 0.
# Si el primer platillo es más pesado, balanza devuelve 1.
# Si el segundo platillo es más pesado, balanza devuelve -1.

# --- DEPENDENCIAS

from utils.tests import *

# balanza ES UNA FUNCION EXTERNA
PESAN_LO_MISMO = 0
PRIMER_PLATILLO_MAS_PESADO = 1
SEGUNDO_PLATILLO_MAS_PESADO = -1
JOYA_VERDADERA = 1

def balanza(arr1, arr2):
    if len(arr1) != len(arr2):
        print('TAMAÑOS NO IGUALES')
    if JOYA_VERDADERA in arr1:
        return PRIMER_PLATILLO_MAS_PESADO
    elif JOYA_VERDADERA in arr2:
        return SEGUNDO_PLATILLO_MAS_PESADO
    else:
        return PESAN_LO_MISMO
    
# --- CODE 

# from balanza import * 

def tiene_tam_par(inicio, final):
    return (final - inicio + 1) % 2 == 0

def dividir_y_pesar(joyas, inicio, final, contador = 0):
    tam = len(joyas)
    if inicio == final or tam <= 2:
        return contador

    contador += 1
    medio = (inicio + final) // 2
    peso_balanza = None

    if tiene_tam_par(inicio, final):
        peso_balanza = balanza(joyas[inicio: medio + 1], joyas[medio+1: final + 1])
    else: 
        peso_balanza = balanza(joyas[inicio: medio], joyas[medio: final])

    
    if peso_balanza == PRIMER_PLATILLO_MAS_PESADO:
        return dividir_y_pesar(joyas, inicio, medio, contador)
    elif peso_balanza == SEGUNDO_PLATILLO_MAS_PESADO:
        return dividir_y_pesar(joyas, medio + 1, final, contador)
    else:
        return contador

def encontrar_joya(joyas):

    inicio = 0
    final = len(joyas) - 1

    cantidad_pesajes = dividir_y_pesar(joyas, inicio, final)

    return cantidad_pesajes


# --- TESTS 
    
tests = [
    [[], 0],
    [[1,0], 0],
    [[0,1], 0],
    [[0,1,0], 1],
    [[1,0,0], 1],
    [[0,0,1], 1],
    [[0, 0, 1, 0, 0], 2],
    [[0, 0, 0, 0, 0, 1], 2],
    [[1, 0, 0, 0, 0, 0], 3],
    [[0, 0, 0, 0, 0, 0, 1], 1], 
]

ejecutar_tests(tests, encontrar_joya)