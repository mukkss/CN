class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
        distance = [float('inf')] * self.vertices
        distance[src] = 0

        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Graph contains a negative-weight cycle")
                return None

        return distance

# Get user input
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))
g = Graph(vertices)

print("Enter each edge in the format: start_vertex end_vertex weight")
for _ in range(edges):
    u, v, weight = map(int, input().split())
    g.add_edge(u, v, weight)

source_vertex = int(input("Enter source vertex: "))
distances = g.bellman_ford(source_vertex)

if distances:
    print("Vertex Distance from Source")
    for i in range(vertices):
        print(f"{i}\t\t{distances[i]}")