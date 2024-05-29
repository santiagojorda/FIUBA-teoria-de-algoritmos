# Implementar un algoritmo de multiplicación de dos números grandes de longitud n,
# por división y conquista, con un orden de complejidad mejor que O(n^2). 
# Justificar el orden del algoritmo mediante el teorema maestro.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea 
# "por división y conquista, en tiempo mejor que O(n^2)". 
# Por las características de la herramienta, no podemos verificarlo de forma automática,
# pero se busca que se implemente con dicha restricción

from tests import *

def ejecutar_multiplicacion(params):
    return multiplicar(params[0], params[1])

# CODIGO

def multiplicar(a, b):
    return karatsuba(a, b)

def partir_num(num, mitad):
    x1 = int(num / (10**mitad))
    x0 = int(num - (x1 * (10**mitad)))
    return [x1, x0]

def karatsuba(a, b):
    tam = len(str(a))
    if tam == 1:
        return a * b

    m = tam // 2

    a1, a0 = partir_num(a,m)
    b1, b0 = partir_num(b,m)

    p = karatsuba(a1 + a0, b1 + b0)
    x0y0 = karatsuba(a0, b0)
    x1y1 = karatsuba(a1, b1)

    t1 = x1y1 * (10**(2*m))
    t2 = (p - x1y1 - x0y0) * (10**m)
    return t1 + t2 + x0y0 

# Algoritmo extraido de:
# https://docs.google.com/presentation/d/1tbBrarxHrmL_OwXyHhE-q6o40EmnRLaSvagpOZ-xN_k/edit#slide=id.g1d4124c8986_0_173

# TESTS

# numero, raiz esperado
lista_tests = [
    [[2, 3], 2*3],
    [[10, 11], 10*11],
    [[100, 100], 100*100],
    [[1000, 1000], 1000*1000],
    [[200, 200], 200*200],
    [[412412, 123142], 412412*123142],
    [[125125125, 125125125], 125125125*125125125]
]
ejecutar_tests(lista_tests, ejecutar_multiplicacion)