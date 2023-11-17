class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in routes:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def add_node(self, key):
        pass

    def add_edge(self, node1_key, node2_key, weight=1):
        pass

    def get_neighbors(self, key):
        pass


if __name__ == '__main__':
    routes = {
        ("New York", "New Jersey"),
        ("New Jersey", "Pennsylvania"),
        ("Pennsylvania", "Maryland"),
        ("Pennsylvania", "West Virginia"),
        ("Maryland", "Virginia"),
        ("Virginia", "North Carolina")
    }

    mygraph = Graph(routes)
    print(mygraph.graph_dict)
