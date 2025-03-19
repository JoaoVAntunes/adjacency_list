from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list) 
        self.order = 0
        self.size = 0   

    def add_node(self, u: str):
        if u in self.adj_list:
            print(f"Node '{u}' already exists.")
            return
        else:
            self.adj_list[u] = []  
            self.order += 1
            print(f"Node '{u}' added successfully.")

    def add_edge(self, u : str, v: str, weight: int):  
        if weight < 0:
            print("Invalid weight.")
            return

        if u not in self.adj_list:
            self.add_node(u)

        if v not in self.adj_list:
            self.add_node(v)

        # Verifies an existing edge, if already exists updates the wieght
        for i, (vertice, p) in enumerate(self.adj_list[u]):
            if vertice == v:
                self.adj_list[u][i] = (v, weight)  
                print(f"Edge between '{u}' and '{v}' updated successfully!")
                return
        
        self.adj_list[u].append((v, weight))
        self.size += 1
        print(f"Edge between '{u}' and '{v}' added successfully!")

    #function to remove a node
    def remove_vertice(self, u):
        if u not in self.adj_list:
            print(f"Vértice '{u}' não existe.")
            return

        # 1. Removes the in degrees edges
        for vertice in list(self.adj_list):  #converting to a list in order to avoid the loop dictionary loop
            original_len = len(self.adj_list[vertice])
            self.adj_list[vertice] = [(v, peso) for v, peso in self.adj_list[vertice] if v != u]
            self.size -= original_len - len(self.adj_list[vertice])

        # 2. Removes the out degrees edges
        self.size -= len(self.adj_list[u]) 
        del self.adj_list[u]

        self.order -= 1

        print(f"Vértice '{u}' e todas as suas arestas foram removidas com sucesso.")

    #function to remove an edge
    def remove_edge(self, u, v):
        if u not in self.adj_list:
            print(f"Node '{u}' does not exist.")
            return
        
        for i, (neighboor, weight) in enumerate(self.adj_list[u]):
            if neighboor == v:
                del self.adj_list[u][i]
                self.size -= 1
                print("Edge was removed!")
                return

        print(f"Aresta de '{u}' para '{v}' não existe.")

    #Verifies if the nodes have and adge in between
    def edge_between(self, u: str, v: str):
        #List Comprehension: "for node, weight in self..." percorre this tuple list trying to find a node equals "v"
        return any(node == v for node, _ in self.adj_list[u])

    #Verifies if the node has any edges
    def there_is_edge(self, u: str):
        return bool(self.adj_list[u])

    #Checks how many edges point to a node 
    def in_degree(self, u):
        if u not in self.adj_list:
            print(f"Node '{u}' does not exists.")
            return
        
        else:
            degree = 0
            for node, edges in self.adj_list.items():
                for v, w in edges:
                    if v == u:
                        degree += 1
            return degree

    #checks the out degree of a node
    def out_degree(self, u):
        if u not in self.adj_list:
            print(f"Node '{u}' does not exists.")
            return
        
        else:
            return len(self.adj_list[u])

    #calculates the total degree (in and out)
    def total_degree(self, u):
        in_deg = self.in_degree(u)
        out_deg = self.out_degree(u)
        
        if in_deg is None or out_deg is None:
            print(f"Error calculating degree for node '{u}'.")
            return None
        
        total_deg = in_deg + out_deg
        return total_deg
    
    #function to get the weight of an edge
    def get_weight(self, u, v):
        for neighboor, weight in self.adj_list[u]:
            if neighboor == v:
                return weight
        print("There is no edge between these nodes.")
        return None

    def toString(self):
        print("\nGraph representation:\n")
        for node, edges in self.adj_list.items():
            if edges:
                print(f"Node {node}: {''.join([f'({v}, {w}) -> ' for v, w in edges])}")
            else:
                print(f"Node {node}: No edges.")
