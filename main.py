from grafo import Graph

def main():
    print("### Testando criação do grafo ###\n")
    G = Graph()

    # Testando adição de vértices
    G.add_node("Pedro")
    G.add_node("Maria")
    G.add_node("Antonio")
    G.add_node("Clara")

    # Testando adição de arestas (com pesos positivos)
    G.add_edge("Pedro", "Maria", 3)
    G.add_edge("Pedro", "Antonio", 1)
    G.add_edge("Maria", "Clara", 2)
    G.add_edge("Clara", "Maria", 5)
    G.add_edge("Pedro", "Clara", 90)


    # Exibindo a lista de adjacência
    G.toString()

    print("\n### Testando consulta de peso da aresta ###")
    print("Peso entre Maria -> Clara:", G.get_weight("Maria", "Clara"))
    print("Peso entre Pedro -> Antonio:", G.get_weight("Pedro", "Antonio"))

    print("\n### Testando verificação de arestas ###")
    print("Existe aresta entre Pedro e Maria?", G.edge_between("Pedro", "Maria"))
    print("Existe aresta entre Antonio e Clara?", G.edge_between("Antonio", "Clara"))

    print("\n### Testando graus ###")
    print("Grau de entrada de Maria:", G.in_degree("Maria"))
    print("Grau de saída de Pedro:", G.out_degree("Pedro"))
    print("Grau total de Clara:", G.total_degree("Clara"))

    print("\n### Testando remoção de aresta (Pedro -> Maria) ###")
    G.remove_edge("Pedro", "Maria")
    G.toString()

    print("\n### Testando remoção de vértice (Maria) ###")
    G.remove_vertice("Maria")
    G.toString()

if __name__ == "__main__":
    main()
