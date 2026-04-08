# Problema do Carteiro Chinês em Dígrafo Ponderado

Este projeto implementa uma solução para o **Problema do Carteiro Chinês** em um dígrafo ponderado, utilizando o **Algoritmo de Hierholzer** para encontrar o circuito euleriano após a eulerização manual do grafo.

## 🚀 Objetivo

O objetivo é percorrer todas as arestas de um dígrafo (grafo direcionado) pelo menos uma vez, retornando ao ponto de origem com o **menor custo total**. 

As etapas realizadas foram:
1.  **Análise Manual:** Identificação de vértices desbalanceados no grafo original.
2.  **Eulerização:** Adição estratégica de arestas para igualar os graus de entrada e saída de cada vértice.
3.  **Implementação:** Desenvolvimento do algoritmo de Hierholzer em Python para extrair o circuito final.

## 📊 Análise do Grafo Oficial (Figura 1)

O grafo oficial processado possui 6 vértices (identificados de `a` a `f`).

### Vértices Desbalanceados Identificados:
| Vértice | Grau de Entrada | Grau de Saída | Status |
| :--- | :---: | :---: | :--- |
| **b (1)** | 2 | 1 | Falta 1 Saída |
| **f (5)** | 1 | 2 | Falta 1 Entrada |

### Justificativa da Eulerização:
Para balancear o grafo, foi adicionada uma aresta direcionada de **b para f** (1 -> 5) com peso 1. Com isso, todos os vértices passaram a ter `Grau de Entrada == Grau de Saída`, tornando o grafo **Euleriano**.

## 💻 Estrutura do Código

O código está organizado em três partes principais:
1.  **Classe `Digraph`:** Gerencia a estrutura de adjacência, graus e pesos.
2.  **Função `find_eulerian_circuit`:** Implementa o método de Hierholzer (similar ao `DirectedEulerianCycle` do *algs4*).
3.  **Execução:** Lê os dados formatados e exibe o circuito e o custo total.

## 🛠️ Como Executar

### No Google Colab:
1. Copie as células de código fornecidas anteriormente.
2. Certifique-se de que a variável `data_eulerizada` contém os dados do grafo balanceado.
3. Execute as células em ordem.

### Localmente (Terminal):
```bash
python hierholzer.py dados/entrada_eulerizada.txt
```

## 📝 Resultados Obtidos
*   **Grafo:** 6 Vértices, 10 Arestas (após eulerização).
*   **Circuito Encontrado:** `a -> c -> b -> f -> c -> e -> f -> e -> d -> b -> a`
*   **Custo Total:** 10

---
*Trabalho desenvolvido com base nos conceitos da disciplina e referências do algs4.*
