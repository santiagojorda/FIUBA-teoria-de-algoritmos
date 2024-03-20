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
