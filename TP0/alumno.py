# La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. 
# En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, 
# hasta llegado un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

# Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

#     Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) 
#     que represente dicha fila, devuelva el índice del alumno más bajo, en tiempo logarítmico.
#     Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel 
#     con altura 0.98.

#     Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) 
#     y un índice, valide (devuelva True o False) si dicho índice corresponde al del alumno 
#     más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante)

# (*)
# Los alumnos son de la forma:

# alumno {
#     nombre (string)
#     altura (float)
# }

# Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

# Importante: considerar que si la prueba de volumen no pasa, es probable que sea porque no 
# están cumpliendo con la complejidad requerida. 

def dividir_y_encontrar_indice_del_mas_chico(alumnos, inicio, final):
    if inicio == final:
        return inicio

    medio = (inicio + final) // 2

    if alumnos[medio].altura < alumnos[medio+1].altura:
        return dividir_y_encontrar_indice_del_mas_chico(alumnos, inicio, medio)
    else:
        return dividir_y_encontrar_indice_del_mas_chico(alumnos, medio+1, final)

def indice_mas_bajo(alumnos):
    inicio = 0
    final = len(alumnos) - 1
    return dividir_y_encontrar_indice_del_mas_chico(alumnos, inicio, final)

def validar_mas_bajo(alumnos, indice):

    tam = len(alumnos)
    inicio = 0
    final = len(alumnos) - 1


    altura_act = alumnos[indice].altura
    siguiente = indice + 1
    anterior = indice - 1
    altura_sig = None
    altura_ant = None

    if indice == inicio:
        altura_sig = alumnos[siguiente].altura
        return altura_act < altura_sig

    altura_ant = alumnos[anterior].altura
    
    if indice == final:
        return altura_act < altura_ant
    else:
        altura_sig = alumnos[siguiente].altura
        return altura_ant > altura_act and altura_act < altura_sig
