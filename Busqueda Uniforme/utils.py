


from grafo import grafo

def calcular_costo(camino):
    """Calcula el costo acumulado de un camino parcial."""
    total = 0
    for i in range(len(camino)-1):
        origen, destino = camino[i], camino[i+1]
        for vecino, costo in grafo[origen]:
            if vecino == destino:
                total += costo
                break
    return total








