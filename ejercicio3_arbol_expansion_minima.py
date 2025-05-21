from datos.ejercicio3_datos import grafo

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v:v for v in vertices}
        self.rank = {v:0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self,root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def Kruskal(graph):
    result = []
    
    vertices = set()
    for u, v, weight in graph:
        vertices.add(u)
        vertices.add(v)
    
    ds = DisjointSet(vertices)
    
    sorted_graph = sorted(graph, key=lambda x: x[2])    
    for u, v, weight in sorted_graph:
        root1 = ds.find(u)
        root2 = ds.find(v)
        
        if root1 != root2:
            result.append((u, v, weight))
            ds.union(root1, root2)
    
    return result

mst = Kruskal(grafo)
print(mst)

