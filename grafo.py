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

    def add_edge(self, u: str, v: str, weight: int):  
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

    #Verifies if the nodes have and adge in between
    def edge_between(self, u: str, v: str):
        #List Comprehension: "for node, weight in self..." percorre this tuple list trying to find a node equals "v"
        return any(node == v for node, weight in self.adj_list[u])

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
            print("The amount of edges pointing to this node is: ", degree)

    def out_degree(self, u):
        if u not in self.adj_list:
            print(f"Node '{u}' does not exists.")
            return
        
        else:
            degree = 0
            for i in enumerate(self.adj_list[u]):
                degree += 1
            print(f"This node has: {degree} edge(s)")


    def toString(self):
        print("\nGraph representation:\n")
        for node, edges in self.adj_list.items():
            if edges:
                print(f"Node {node}: {''.join([f'({v}, {w}) -> ' for v, w in edges])}")
            else:
                print(f"Node {node}: No edges.")
