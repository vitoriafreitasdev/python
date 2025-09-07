

from collections import defaultdict
class Graph:
    def __init__(self, edges):
        self.edges = edges

        self.graph_dict =  {} # ou usando defaultdict(list)

        # com o defaultdict(list)
        # for start, end in self.edges:
        #     self.graph_dict[start].append(end)
        #     self.graph_dict[end].append(start)

        for start, end in self.edges:
            # adiciona start → end
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            # para grafo nao direcionado
            # # adiciona end → start
            # if end in self.graph_dict:
            #     self.graph_dict[end].append(start)
            # else:
            #     self.graph_dict[end] = [start]


        print("Graph dict", self.graph_dict)

    def get_paths(self, start, end, path=[]): # algoritmo dfs
        path = path + [start]
       
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:

                new_paths = self.get_paths(node, end, path)
                
                for p in new_paths:
                    paths.append(p) 

        return paths # paths vai acumular as resposta função recursiva get_paths
    
    def get_shortest_path(self, start, end, path=[]): # algoritmo parecido com bfs
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None 
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:

                sp = self.get_shortest_path(node, end, path)

                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),

    ]

    routes_graph = Graph(routes)
    
    start = "Toronto"
    end = "Mumbai"

    print("Shortest paths: ", routes_graph.get_shortest_path(start, end))