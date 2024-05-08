# Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique 
# (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

# Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo,
# está disponible como se describe.

# --- 


def es_seguro(tablero, fila, col, N):
    # Verifica si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False
    
    # Verifica la diagonal izquierda arriba
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Verifica la diagonal derecha arriba
    i, j = fila - 1, col + 1
    while i >= 0 and j < N:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def resolver_n_reinas_util(tablero, fila, N, reinas):
    if fila >= N:
        return True
    
    for col in range(N):
        if es_seguro(tablero, fila, col, N):
            tablero[fila][col] = 1
            reinas.append((fila, col))

            if resolver_n_reinas_util(tablero, fila+1, N, reinas):
                return True
            
            # Si colocar la reina en tablero[fila][col] no conduce a una solución, retroceder
            tablero[fila][col] = 0
            reinas.pop()
    
    return False

def nreinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    reinas = []
    resolver_n_reinas_util(tablero, 0, n, reinas)
    return reinas

nreinas(2)