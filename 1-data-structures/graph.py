class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print('Graph Dict:', self.graph_dict)

    def get_full_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        full_path = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_full_path = self.get_full_path(node, end, path)

                for path in new_full_path:
                    full_path.append(path)

        return full_path
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                new_shortest_path = self.get_shortest_path(node, end, path)

                if new_shortest_path:
                    if shortest_path is None or len(shortest_path) > len(new_shortest_path):
                        shortest_path = new_shortest_path

        return shortest_path
    
if __name__ == '__main__':
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    route_graph = Graph(routes)
    
    start = 'Mumbai'
    end = 'Bangaluru'

    print(f'All paths between: {start} and {end}:', route_graph.get_full_path(start, end))
    print(f'Shortest path between {start} and {end}:', route_graph.get_shortest_path(start, end))