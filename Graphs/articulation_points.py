from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.Time = 0
        self.low = [float('inf')] * self.vertices
        self.parent = [-1] * self.vertices
        self.dist = [float("inf")] * self.vertices
        self.ap = [False] * self.vertices
        self.visited = [False] * self.vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # since this graph is undirected

    def articulation_point(self, node):
        # mark node visited
        self.visited[node] = True

        # self.Time tracks node visit order
        self.low[node] = self.Time
        self.dist[node] = self.Time
        self.Time += 1

        for v in self.graph[node]:
            if not self.visited[v]:
                self.parent[v] = node
                self.articulation_point(v)
                self.low[node] = min(self.low[v], self.low[node])
                # root check here since root can never be articulation point
                if self.parent[node] != -1 and self.low[v] >= self.dist[node]:
                    self.ap[node] = True
            elif v != self.parent[node]:
                self.low[node] = min(self.low[node], self.dist[v])


if __name__ == '__main__':
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)

    for v in g1.graph.keys():
        if not g1.visited[v]:
            g1.articulation_point(v)

    for index, value in enumerate(g1.ap):
        if value == True:
            print(f"Articulation Point {index}")
