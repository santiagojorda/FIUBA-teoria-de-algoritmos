# Implementar un algoritmo de multiplicación de dos números grandes de longitud n,
# por división y conquista, con un orden de complejidad mejor que O(n^2). 
# Justificar el orden del algoritmo mediante el teorema maestro.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea 
# "por división y conquista, en tiempo mejor que O(n^2)". 
# Por las características de la herramienta, no podemos verificarlo de forma automática,
# pero se busca que se implemente con dicha restricción


def multiplicar(a, b):
    return 0







# TESTS

def ejecutar_tests(lista_tests, funcion):    
    exitos = 0
    fallos = 0

    for i, test in enumerate(lista_tests): 
        num1, num2, esperado = test
        calculado = funcion(num1, num2)
        print("\n",
            f"- CASO {i + 1}\n", 
            f"Numeros: {num1} * {num2}\n", 
            f"Multiplicacion esperada: {num1 * num2} \n",
            f"Multiplicacion calculada: {calculado}")
        if calculado == esperado:
            print("")
            exitos = exitos + 1
        else:
            print("--------- FALLO\n")
            fallos = fallos + 1

    print(f"RESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")

# numero, raiz esperado
lista_tests = [
    [10, 10, 100],
    [20, 20, 400],
    [412412, 123142, 50785238504],
    [1, 1, 1],
    [0, 125125125125, 0],
    [125125125125, 125125125125, 15656296937546906265625]
]
ejecutar_tests(lista_tests, multiplicar)