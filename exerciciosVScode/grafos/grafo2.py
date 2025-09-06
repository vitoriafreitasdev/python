
class Graph:
    def __init__(self, edges):
        self.edges = edges

        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                pass
            else:
                self.graph_dict[start] = [end]











if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),

    ]

    route_graph = Graph(routes)