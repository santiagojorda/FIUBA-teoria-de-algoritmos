# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
# Además, cada charla tiene asociado un valor de ganancia. 
# Implementar un algoritmo que, utilizando programación dinámica, 
# reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, 
# fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar 
# la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

from tests import *

# CODIGO

def scheduling(charlas):
    pass


# TESTS

tests = [
    [0, 1],
    [1, 1],
    [2, 2],
    [3, 3],
    [8, 34]
]

ejecutar_tests(tests, scheduling)