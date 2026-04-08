import sys
import os
from digraph import Digraph
from hierholzer import Hierholzer

def read_graph(filename):
    """Lê o grafo de um arquivo no formato V, E, v w peso."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Arquivo {filename} não encontrado.")
        
    with open(filename, 'r') as f:
        lines = f.readlines()
        V = int(lines[0].strip())
        E = int(lines[1].strip())
        graph = Digraph(V)
        for i in range(2, 2 + E):
            v, w, weight = map(int, lines[i].split())
            graph.add_edge(v, w, weight)
    return graph

def main():
    """Ponto de entrada do programa."""
    if len(sys.argv) < 2:
        filename = "dados/entrada_eulerizada.txt"
    else:
        filename = sys.argv[1]
        
    try:
        graph = read_graph(filename)
        
        print(f"--- Análise do Grafo: {filename} ---")
        print(f"Vértices: {graph.V}, Arestas: {graph.E}")
        print("Graus dos vértices:")
        print("Vértice | In-Degree | Out-Degree | Status")
        print("--------|-----------|------------|-------")
        
        for i in range(graph.V):
            status = "OK" if graph.in_degree[i] == graph.out_degree[i] else "DESBALANCEADO"
            print(f"   {i}    |     {graph.in_degree[i]}     |      {graph.out_degree[i]}     | {status}")
            
        if not graph.is_balanced():
            print("\nErro: O grafo não está balanceado. Não é possível encontrar um circuito euleriano.")
            return

        # Executar o algoritmo de Hierholzer
        solver = Hierholzer(graph)
        circuit, total_cost, success = solver.find_circuit()
        
        if success:
            print("\nCircuito Euleriano encontrado:")
            # Converter índices de volta para letras (0=a, 1=b, ...)
            nodes = "abcdefghijklmnopqrstuvwxyz"
            circuit_letters = [nodes[v] for v in circuit]
            print(" -> ".join(circuit_letters))
            print(f"\nCusto Total do Circuito: {total_cost}")
        else:
            print("\nNão foi possível encontrar um circuito euleriano.")
            
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
