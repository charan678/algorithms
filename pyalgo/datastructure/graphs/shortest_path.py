from pyalgo.datastructure.graphs.graph import Graph


class Shortest(Graph):

    def __init__(self, vertices):
        super().__init__(vertices)

    def dijasktra(self, source, target):
        distances[source] = 0
        distances = [100000 for i in range(0, self.V)]




    def optimized(self):
        pass

if __name__  == "__main__":
    graph = Shortest(6)
    graph.add_link((0, 1, 10))
    graph.add_link((0, 2, 10))
    graph.add_link((1, 3, 10))
    graph.add_link((2, 4, 10))
    graph.add_link((2, 3, 10))
    graph.add_link((3, 5, 10))
    graph.add_link((4, 5, 10))
    print("*"*50)
    graph.dijasktra()
    print("#"*50)