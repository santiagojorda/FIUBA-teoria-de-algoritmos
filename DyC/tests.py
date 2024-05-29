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

    print(f"RESUMEN TESTS \n",
          f"    Exitos: {exitos} \n",
          f"    Fallos: {fallos} \n")