from collections import defaultdict

class Digraph:
    """
    Representação de um dígrafo ponderado.
    Inspirado na estrutura do algs4.
    """
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = defaultdict(list)
        self.in_degree = [0] * V
        self.out_degree = [0] * V

    def add_edge(self, v, w, weight):
        """Adiciona uma aresta direcionada de v para w com o peso indicado."""
        self.adj[v].append({'to': w, 'weight': weight, 'used': False})
        self.out_degree[v] += 1
        self.in_degree[w] += 1
        self.E += 1

    def is_balanced(self):
        """Verifica se o grau de entrada é igual ao grau de saída para todos os vértices."""
        for i in range(self.V):
            if self.in_degree[i] != self.out_degree[i]:
                return False
        return True

    def get_total_weight(self):
        """Calcula a soma dos pesos de todas as arestas no grafo."""
        total = 0
        for u in range(self.V):
            for edge in self.adj[u]:
                total += edge['weight']
        return total
