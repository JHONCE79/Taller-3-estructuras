import json
def bottleneck(graph):
    bottleneck_edge = None
    bottleneck_weight = float('inf')
    for edge in graph.edges:
        weight = edge.weight
        
    




with open("datos/ejercicio2_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
inicio = datos["inicio"]
objetivo = datos["objetivo"]