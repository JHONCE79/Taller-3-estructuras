🚀 Ejercicio 1: Rutas óptimas entre servicios de una arquitectura distribuida
Contexto: En una arquitectura de microservicios distribuida, los servicios se comunican entre sí mediante enlaces de red con diferentes niveles de latencia. Para realizar pruebas o diagnósticos, necesitas encontrar la ruta más rápida entre dos servicios.

Tarea: Implementa una función que, dado un grafo dirigido ponderado (donde los nodos son servicios y los pesos son milisegundos de latencia), encuentre el camino de menor latencia entre un servicio origen y uno destino.

Tips:

Modela el grafo como un diccionario de adyacencias.
Aplica el algoritmo de Dijkstra para obtener el camino más corto.
Además de la distancia, también retorna el camino seguido.
Datos de prueba:

grafo = {
    "frontend": {"auth": 20, "search": 50},
    "auth": {"db": 10},
    "search": {"db": 5},
    "db": {"storage": 15},
    "storage": {}
}

origen = "frontend"
destino = "storage"
Resultado esperado:

Camino más corto: ["frontend", "auth", "db", "storage"]
Costo total: 45
(También sería válido si se encuentra la otra ruta con igual costo si existiera; lo importante es que sea una ruta mínima).

🧭 Ejercicio 2: Análisis de cuellos de botella en flujos de navegación
Contexto: Has recolectado datos sobre cómo los usuarios navegan por tu sistema web. Quieres encontrar las vistas que podrían estar sobrecargadas, porque muchos caminos de navegación pasan por ellas.

Tarea: Dado un grafo dirigido ponderado que representa la frecuencia de navegación entre páginas, encuentra los nodos (vistas) que están en más rutas desde la página inicial hacia una sección crítica.

Tips:

Utiliza BFS o DFS para recorrer todos los caminos posibles.
Cuenta cuántas rutas pasan por cada nodo intermedio.
Puedes usar diccionarios para llevar conteos de visitas.
Datos de prueba:

grafo = {
    "home": {"login": 10, "search": 5},
    "login": {"dashboard": 8},
    "search": {"dashboard": 4, "details": 6},
    "dashboard": {"details": 7},
    "details": {}
}

inicio = "home"
objetivo = "details"
Resultado esperado: Un diccionario con la cantidad de rutas en las que cada nodo intermedio aparece (solo para nodos intermedios):

{
    "login": 1,
    "dashboard": 2,
    "search": 2
}
Esto indica que dashboard y search están involucrados en múltiples caminos desde home hasta details.

🛰️ Ejercicio 3: Optimización del monitoreo distribuido
Contexto: Estás diseñando una red de monitoreo entre servidores. Necesitas conectar todos los nodos minimizando el costo de comunicación total, pero garantizando que todos estén conectados directamente o indirectamente.

Tarea: A partir de un grafo no dirigido y ponderado, encuentra el árbol de expansión mínima (MST).

Tips:

Puedes aplicar Prim o Kruskal.
Asegúrate de evitar ciclos.
Usa estructuras eficientes como colas de prioridad o conjuntos disjuntos.
Datos de prueba:

grafo = {
    "A": [("B", 3), ("C", 1)],
    "B": [("A", 3), ("C", 7), ("D", 5)],
    "C": [("A", 1), ("B", 7), ("D", 2)],
    "D": [("B", 5), ("C", 2)]
}
Resultado esperado: Una lista de aristas en el MST y el costo total:

MST = [("A", "C", 1), ("C", "D", 2), ("A", "B", 3)]
Costo total = 6