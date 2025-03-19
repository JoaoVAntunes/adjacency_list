import grafo as graph

G = graph.Graph()
G.add_node("Joao")
G.add_node("Maria")
G.add_edge("Joao", "Maria", 3)
G.add_edge("Joao", "Caio", 60)
G.add_edge("Maria", "Clara", 99)


# print("\n", G.edge_between("Joao", "Maria"))
# print(G.edge_between("Joao", "Clara"))

# print("\n", G.there_is_edge("Joao"))
# print(G.there_is_edge("Caio"))

#G.in_degree("Maria")
G.out_degree("Joao")


G.toString()
