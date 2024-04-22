# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada 
# cantidad de plata. Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima 
# cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, 
# y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados 
# para minimizar la cantidad total utilizada. Indicar y justificar la complejidad del algoritmo implementado. 
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. 
# ¿Por qué se trata de un algoritmo Greedy? Justificar

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". 
# Por las características de la herramienta, no podemos verificarlo de forma automática, 
# pero se busca que se implemente con dicha restricción

# ---------------------------

# La característica principal de los algoritmos greedy es que toman decisiones locales óptimas
# en cada paso con la esperanza de encontrar una solución global óptima. 
# Esto significa que en cada paso, el algoritmo elige la mejor opción disponible en ese momento 
# sin considerar las consecuencias a largo plazo.
# Un algoritmo greedy puede o no encontrar la solucion optima
# En caso de que la encuentre, a este se le llama "canonico"

# El algoritmo implementado es conocido como "Solucion del cajero" 
# Se trata de un algoritmo greedy, pero este no devuelve una solucion optima. Por ende no es canonico. 

# Dado el ejemplo dado en el video: Mochila fraccionaria y cambio de moneda[1]

# La complejidad algoritmica es O(n)

# Con el siguiente contra ejemplo, se puede verificar que el algoritmo no es optimo.

# Contra ejemplo: 

# cambio = [1, 2, 4, 5, 10], monto = 8

# el algoritmo no da la solucion optima que seria [4, 4] -> 2 monedas
# sino que devuelve mas cantidad de monedas [5, 2, 1] -> 3 monedas
#
# [1] Mochila fraccionaria y cambio de moneda:
# https://www.youtube.com/watch?v=MwBq72jmz58&list=PLzVbItixzlGUYKjuyaqa5qm9ZyZDfkXym&index=6&ab_channel=vpode


def cambio(monedas, monto):

    tam = len(monedas)

    sum_parcial = 0
    i = tam-1

    cambio_minimo = []

    while sum_parcial != monto:
        sum_aux = monedas[i] + sum_parcial
        if sum_aux <= monto:
            sum_parcial = sum_aux
            cambio_minimo.append(monedas[i])
        else:
            i -= 1

    return cambio_minimo




# TESTS 

def ejecutar_tests(lista_tests, funcion):    
    exitos = 0
    fallos = 0

    for i, test in enumerate(lista_tests): 
        monedas, monto, esperado = test
        calculado = funcion(monedas, monto)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"Monedas: {monedas} \n", 
            f"Monto: {monto} \n", 
            f"Cambio esperado: {esperado} \n",
            f"cambio calculada: {calculado}")
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
monedas1 = [1, 2, 5]
monto1 = 11

monedas2 = []
monto2 = 0

monedas3 = [1, 5, 10]
monto3 = 1

monedas4 = [1, 5, 10]
monto4 = 11

monedas5 = [1, 2, 4, 5, 10]
monto5 = 8
tests = [
    [monedas1, monto1, [5, 5, 1]],
    [monedas2, monto2, []],
    [monedas3, monto3, [1]],
    [monedas4, monto4, [10, 1]],
    [monedas5, monto5, [4, 4]],
]

ejecutar_tests(tests, cambio)