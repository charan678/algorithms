class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.links = []

    def add_link(self, value):
        self.links.append(value)

    def bfs(self):
        is_visited = [False for i in range(0, self.V)]
        queue = [0]
        is_visited[0] = True
        while len(queue) != 0:
            vertice = queue.pop(0)
            print("vertice = ", vertice)
            for val in self.links:
                if val[0] == vertice:
                    if not is_visited[val[1]]:
                        queue.append(val[1])
                        is_visited[val[1]] = True

    def dfs(self, vertix=0, is_visited=[True, False, False, False, False, False]):
        if False not in is_visited:
            return
        is_visited[vertix] = True
        print("vertix = ", vertix)
        for link in self.links:
            if link[0] == vertix:
                self.dfs(link[1], is_visited)

    def topological(self):
        topo_order = []
        levels = [0 for i in range(0, self.V)]
        is_visited = [False for i in range(0, self.V)]
        for link in self.links:
            levels[link[1]] += 1
        while True:
            for index, level in enumerate(levels):
                if not is_visited[index] and level == 0:
                    topo_order.append(index)
                    is_visited[index] = True
                    for i in self.links:
                        if i[0] == index:
                            levels[i[1]] -= 1
            if False not in is_visited:
                break
        for val in topo_order:
            print(val)

    def has_cycles(self):
        has_cycle = 0
        levels = [0 for i in range(0, self.V)]
        is_visited = [False for i in range(0, self.V)]
        for link in self.links:
            levels[link[1]] += 1
        while True:
            for index, level in enumerate(levels):
                if level == 0:
                    is_visited[index] = True
                    for i in self.links:
                        if i[0] == index:
                            levels[i[1]] -= 1
                            if levels[i[1]] < 0:
                                has_cycle = True
                                break
                    if has_cycle or False not in is_visited:
                        break
        return has_cycle

if __name__ == "__main__":
    graph = Graph(6)
    graph.add_link((0, 1, 10))
    graph.add_link((0, 2, 10))
    graph.add_link((1, 3, 10))
    graph.add_link((2, 4, 10))
    graph.add_link((2, 3, 10))
    graph.add_link((3, 5, 10))
    graph.add_link((4, 5, 10))
    #graph.dfs()
    print("*"*40)
    #graph.bfs()
    print("*"*50)
    graph.has_cycles()
    print("#"*50)