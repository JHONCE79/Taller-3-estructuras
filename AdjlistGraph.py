class AdjListGraph:
    def __init__(self):
      self.adj_list = {}

    def add_vertex(self, vertex):
      if vertex not in self.adj_list:
        self.adj_list[vertex] = []

    def add_edge(self, src, dest, weight = 1):
      if src in self.adj_list:
        self.adj_list[src].append((dest, weight))
        #self.adj_list[dest].append((src, weight))
      else:
        raise ValueError(f"Source vertex {src} not in graph")

    def remove_edge(self, src, dest):
      if src in self.adj_list:
        if dest in self.adj_list[src]:
          self.adj_list[src].remove(dest)

    def get_neighbors(self, vertex) -> list:
      return self.adj_list.get(vertex, [])

    def get_nodes(self) -> list:
      return list(self.adj_list.keys())

    def dfs(self, src, visited = None, key=print):
      if not visited:
        visited = set()
      visited.add(src)
      key(src)
      for neighbor in self.adj_list[src]:
        if neighbor not in visited:
          self.dfs(neighbor, visited, key)

    def dfs_iterative(self, src, key=print):
      stack = [src]
      visited = set()
      while stack:
        vertex = stack.pop()
        if vertex not in visited:
          visited.add(vertex)
          key(vertex)
          for neighbor in reversed(self.adj_list[vertex]):
            if neighbor not in visited:
              stack.append(neighbor)

    def bfs(self, src, key=print):
      queue = [src]
      visited = set()
      while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
          visited.add(vertex)
          key(vertex)
          for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
              queue.append(neighbor)