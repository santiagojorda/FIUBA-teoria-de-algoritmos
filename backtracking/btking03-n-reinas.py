# Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique 
# (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

# Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo,
# está disponible como se describe.

# --- 

def nreinas(n):
    return [(0, 0)]