def encontrar_ruta(C):

    res = [ [ 1 for j in range(len(C[0])) ] for i in range(len(C)) ] 

    if encontrar_ruta_aux(C, 0, 0, res, 'down') == False: 
        return []

    negar_matriz(res)

    return res
    

def encontrar_ruta_aux(C, x, y, res, direction):

    if x == len(C) - 1 and y == len(C[0]) - 1 and C[x][y]== 0:                    
        res[x][y] = 0
        return True

    if es_camino_seguro(C, x, y):
        res[x][y] = 0
 
        if direction != 'up' and encontrar_ruta_aux(C, x + 1, y, res, 'down'):                                       # Movimiento hacia abajo
            return True
        # En caso de que moverse hacia abajo no de una solucion entonces intentamos por la derecha

        # Esto lo hacemos moviendonos por la columna de la matriz
        if direction != 'left' and encontrar_ruta_aux(C,x, y + 1, res, 'right'):                                     # Movimiento a la derecha
            return True
        # Si no funciona intentamos moviendomos hacia arriba
        if direction != 'down' and direction != 'left' and encontrar_ruta_aux(C, x - 1, y, res, 'up'):               # Movimiento hacia la izquierda
            return True
        # Como ultima alternativa hacemos el intento moviendonos a la izquierda

        if direction != 'right ' and direction != 'up' and encontrar_ruta_aux(C, x, y - 1, res, 'left'):             # Movimiento hacia arriba
            return True
        
        # En caso de que ninguna funcione hacemos el backtracking
        res[x][y] = 1
        return False

# Metodo para negar la matriz y mostrar el camino correcto con 1 en vez de 0

def negar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (matriz[i][j] == 1):
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
    return matriz

# Funcion que se encarga de determinar si un camino es seguro o no

def es_camino_seguro( C, x, y ):

    if x >= 0 and x < len(C) and y >= 0 and y < len(C[0]) and C[x][y] == 0: 
        return True
      
    return False








