class Hierholzer:
    """
    Implementação do algoritmo de Hierholzer para encontrar um circuito euleriano.
    Baseado no DirectedEulerianCycle do algs4.
    """
    def __init__(self, graph):
        self.graph = graph
        self.circuit = []
        self.success = False
        self.total_cost = 0

    def find_circuit(self, start_node=0):
        """Executa o algoritmo para encontrar o circuito euleriano."""
        if not self.graph.is_balanced():
            self.success = False
            return None, 0, False

        # Cópia das listas de adjacência para não destruir o grafo original
        adj_copy = {v: [edge for edge in edges] for v, edges in self.graph.adj.items()}
        
        curr_path = [start_node]
        circuit_result = []
        
        while curr_path:
            u = curr_path[-1]
            
            # Encontrar uma aresta não usada saindo de u
            found_edge = False
            for i in range(len(adj_copy[u])):
                if not adj_copy[u][i]['used']:
                    adj_copy[u][i]['used'] = True
                    curr_path.append(adj_copy[u][i]['to'])
                    found_edge = True
                    break
            
            if not found_edge:
                circuit_result.append(curr_path.pop())
        
        self.circuit = circuit_result[::-1]
        self.total_cost = self.graph.get_total_weight()
        self.success = True
        return self.circuit, self.total_cost, True
