from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.order = 0
        self.size = 0

    def add_node(self, u):
        if u in self.adj_list:
            print("Node already exists")
            return
        else:
            self.adj_list = u
            self.order += 1
            print("Node addded succesfully ")

    def add_edge(self, u, v, weight):  
        if weight < 0:
            print("Invalid weight")
            return

        elif u not in self.adj_list:
            self.add_node(u)

        elif v not in self.adj_list:
            self.add_node(v)

        # Verifica se a aresta já existe e atualiza o peso
        for i, (vertice, p) in enumerate(self.adj_list[u]):
            if vertice == v:
                self.adj_list[u][i] = (v, weight)
                print("Edge updated successfully!")
                return
        
        self.adj_list[u].append((v, weight))
        self.size += 1
        print("Edge added succesfully!")
    
    def edge_between(self, u, v):
        #List Comprehension: "for node, weight in self..." percorre this tuple list trting to find a node equals "v"
        return any( node == v for node, weight in self.adj_list[u])
    
    def there_is_edge(self, u):
          return bool(self.adj_list[u])

