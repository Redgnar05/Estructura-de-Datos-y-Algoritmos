


import heapq

class BusquedaUniforme:
    def __init__(self, grafo, archivo_salida="salida_busqueda_uniforme.txt"):
        self.grafo = grafo
        self.archivo_salida = archivo_salida

    def buscar(self, inicio, objetivo):
        cola = [(0, inicio, [inicio])]
        visitados = set()
        iteracion = 0

        with open(self.archivo_salida, 'w', encoding='utf-8') as f:
            while cola:
                f.write(f"\n Nodos visitados: {visitados}\n")
                f.write(f"\n🔁 Iteración {iteracion}\n")
                f.write("Estado actual del heap:\n")
                for item in cola:
                    f.write(f"  Costo: {item[0]:3} | Nodo: {item[1]:13} | Camino: {item[2]}\n")

                costo, nodo, camino = heapq.heappop(cola)
                f.write(f"\n➡️ Expandiendo nodo: {nodo} con costo acumulado: {costo}\n")

                if nodo in visitados:
                    f.write("⚠️ Ya fue visitado. Se omite.\n")
                    iteracion += 1
                    continue

                visitados.add(nodo)

                if nodo == objetivo:
                    f.write("🎯 ¡Nodo objetivo encontrado!\n")
                    f.write(f"\n✅ Camino más barato: {camino}\n")
                    f.write(f"💰 Costo total: {costo}\n")
                    return camino, costo

                for vecino, peso in self.grafo.get(nodo, []):
                    if vecino not in visitados:
                        heapq.heappush(cola, (costo + peso, vecino, camino + [vecino]))
                        f.write(f"➕ Agregado al heap: {vecino} con costo {costo + peso}\n")

                iteracion += 1

            f.write("\n❌ No se encontró un camino.\n")
            return None, float('inf')





