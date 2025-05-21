import json
import heapq

def dijkstra(graph, source, target):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    path = {node: [] for node in graph}
    path[source] = [source]
    queue = [(0, source)]
    
    while queue:
        actual_distance, node_actual = heapq.heappop(queue)
        
        if actual_distance > distances[node_actual]:
            continue
            
        for neighboor, weight in graph[node_actual].items():
            distance = actual_distance + weight
            
            if distance < distances[neighboor]:
                distances[neighboor] = distance
                path[neighboor] = path[node_actual] + [neighboor]
                heapq.heappush(queue, (distance, neighboor))
    
    return path[target], distances[target]

with open("datos/ejercicio1_datos.json") as f:
    data = json.load(f)

graph = data["grafo"]
source = data["origen"]
target = data["destino"]

path, cost = dijkstra(graph, source, target)

print(f"shortest path: {path}")
print(f"total cost: {cost}")