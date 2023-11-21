import heapq


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in routes:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def add_node(self, start, end):
        if start not in self.graph_dict:
            self.graph_dict[start] = [end]
        else:
            if end not in self.graph_dict[start]:
                self.graph_dict[start].append(end)

    def remove_node(self, node):
        if node in self.graph_dict:
            # Delete the node itself
            del self.graph_dict[node]

            # Remove edges connected to the node from other vertices
            for start, edges in self.graph_dict.items():
                if node in edges:
                    self.graph_dict[start] = [edge for edge in edges if edge != node]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]  # Return a list containing the path as a list

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path[:])  # Pass a copy of the path
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end):
        paths = self.get_paths(start, end)
        shortest_path = None
        for path in paths:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path
        return shortest_path

    """
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph_dict}
        distances[start] = 0
    
        priority_queue = [(0, start)]  # (distance, node)
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
    
            # Check if the current distance is greater than the known shortest distance
            if current_distance > distances[current_node]:
                continue
    
            for neighbor in self.graph_dict.get(current_node, []):
                distance = current_distance + 1  # Assuming unit weights
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
        return distances
    """


if __name__ == '__main__':
    routes = {
        ("New York", "New Jersey"),
        ("New Jersey", "Pennsylvania"),
        ("Pennsylvania", "Maryland"),
        ("Pennsylvania", "West Virginia"),
        ("Maryland", "Virginia"),
        ("Virginia", "North Carolina"),
        ("New York", "South Carolina")
    }

    mygraph = Graph(routes)
    mygraph.add_node("North Carolina", "South Carolina")
    print(mygraph.graph_dict)
    print(mygraph.get_shortest_path("New York", "South Carolina"))

