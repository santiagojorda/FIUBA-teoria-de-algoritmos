
# Implementar un algoritmo que, utilizando programación dinámica, 
# obtenga el valor del n-ésimo número de fibonacci. 
# Indicar y justificar la complejidad del algoritmo implementado.

# Definición:
# n = 0 --> Debe devolver 1
# n = 1 --> Debe devolver 1
# n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
# Por las características de la herramienta, no podemos verificarlo de forma automática,
# pero se busca que se implemente con dicha restricción

from tests import *

# CODIGO

def fibonacci(n):
    if (n == 0 or n == 1):
        return 1
    M_FIB = [None] * (n+1)
    M_FIB[0] = 1
    M_FIB[1] = 1
    for i in range(2, n+1):
        M_FIB[i] = M_FIB[i-1] + M_FIB[i-2]
    return M_FIB[n] 


# TESTS

tests = [
    [0, 1],
    [1, 1],
    [2, 2],
    [3, 3],
    [8, 34]
]

ejecutar_tests(tests, fibonacci)