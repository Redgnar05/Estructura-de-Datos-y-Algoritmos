


conexiones = [("Oradea", "Zerind", 71),
              ("Oradea", "Sibiu", 151),
              ("Zerind", "Arad", 75),
              ("Arad", "Sibiu", 140),
              ("Arad", "Timisoara", 118),
              ("Timisoara", "Lugoj", 111),
              ("Lugoj", "Mehadia", 70),
              ("Mehadia", "Dobreta", 75),
              ("Sibiu", "Fagaras", 99),
              ("Sibiu", "Rmnicu Vilcea", 80),
              ("Rmnicu Vilcea", "Craiova", 146),
              ("Dobreta", "Craiova", 120),
              ("Rmnicu Vilcea", "Pitesti", 97),
              ("Pitesti", "Craiova", 138),
              ("Fagaras", "Bucharest", 211),
              ("Pitesti", "Bucharest", 101),
              ("Bucharest", "Giurgiu", 90),
              ("Bucharest", "Urziceni", 85),
              ("Urziceni", "Hirsova", 98),
              ("Hirsova", "Eforie", 86),
              ("Urziceni", "Vaslui", 142),
              ("Vaslui", "Iasi", 92),
              ("Iasi", "Neamt", 87)]

# Construcción del grafo como diccionario
grafo = {}

for origen, destino, costo in conexiones:
    # Agregar conexión origen -> destino
    if origen not in grafo:
        grafo[origen] = []
    grafo[origen].append((destino, costo))

    # Agregar conexión destino -> origen
    if destino not in grafo:
        grafo[destino] = []
    grafo[destino].append((origen, costo))





