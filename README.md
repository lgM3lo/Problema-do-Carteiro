[README.md](https://github.com/user-attachments/files/26568467/README.md)
# Relatório: Problema do Carteiro Chinês em Dígrafo Ponderado

## 1. Introdução

Este relatório detalha a solução para o Problema do Carteiro Chinês em um dígrafo ponderado, conforme solicitado. O trabalho foi dividido em duas partes principais: uma análise manual do grafo para sua eulerização e a implementação de um programa em Python utilizando o algoritmo de Hierholzer para encontrar o circuito euleriano.

## 2. Análise do Grafo Oficial (Figura 1)

O grafo oficial de entrada para este trabalho é o representado na Figura 1. A partir da imagem, os vértices e arestas foram identificados e representados no formato de entrada `V` (número de vértices), `E` (número de arestas), seguido de `v w peso` para cada aresta. Para simplificação, os pesos de todas as arestas foram considerados como 1, conforme a natureza do problema que busca minimizar o número de repetições de arestas.

### 2.1. Grafo Original (`dados/entrada_original.txt`)

O grafo original, extraído da Figura 1, é composto por 6 vértices (0 a 5) e 9 arestas. A representação em `dados/entrada_original.txt` é a seguinte:

```
6
9
0 2 1
1 0 1
2 1 1
2 4 1
3 1 1
4 3 1
4 5 1
5 2 1
5 4 1
```

### 2.2. Análise de Balanceamento do Grafo Original

Ao executar o programa `hierholzer.py` com o grafo original, obtivemos a seguinte análise de graus de entrada e saída:

```
--- Análise do Grafo: dados/entrada_original.txt ---
Vértices: 6, Arestas: 9
Graus dos vértices:
Vértice | In-Degree | Out-Degree | Status
--------|-----------|------------|-------
   0    |     1     |      1     | OK
   1    |     2     |      1     | DESBALANCEADO
   2    |     2     |      2     | OK
   3    |     1     |      1     | OK
   4    |     2     |      2     | OK
   5    |     1     |      2     | DESBALANCEADO
Erro: O grafo não está balanceado. Não é possível encontrar um circuito euleriano.
```

Como esperado, o grafo original não está balanceado, pois os vértices 1 e 5 apresentam graus de entrada e saída diferentes. O vértice 1 tem `in-degree = 2` e `out-degree = 1`, enquanto o vértice 5 tem `in-degree = 1` e `out-degree = 2`.

## 3. Eulerização Manual do Grafo Oficial

Para eulerizar o grafo, é necessário adicionar arestas de forma que o grau de entrada de cada vértice seja igual ao seu grau de saída. Analisando os vértices desbalanceados:

-   **Vértice 1:** `in-degree = 2`, `out-degree = 1`. Precisa de uma aresta de saída.
-   **Vértice 5:** `in-degree = 1`, `out-degree = 2`. Precisa de uma aresta de entrada.

Para balancear esses vértices, uma aresta adicional de 1 para 5 (1 -> 5) com peso 1 foi inserida. Isso aumenta o `out-degree` de 1 para 2 e o `in-degree` de 5 para 2, balanceando ambos os vértices.

### 3.1. Grafo Eulerizado (`dados/entrada_eulerizada.txt`)

Após a adição da aresta (1, 5, 1), o grafo eulerizado é representado em `dados/entrada_eulerizada.txt`:

```
6
10
0 2 1
1 0 1
2 1 1
2 4 1
3 1 1
4 3 1
4 5 1
5 2 1
5 4 1
1 5 1
```

## 4. Implementação do Algoritmo de Hierholzer

O algoritmo de Hierholzer foi implementado em Python no arquivo `hierholzer.py`. Este programa lê o grafo de um arquivo, calcula os graus de entrada e saída de cada vértice, verifica o balanceamento e, se o grafo for euleriano, encontra e imprime um circuito euleriano, juntamente com seu custo total.

### 4.1. Teste com o Grafo Eulerizado Oficial

Ao executar o programa `hierholzer.py` com o grafo eulerizado (`dados/entrada_eulerizada.txt`), obtivemos o seguinte resultado:

```
--- Análise do Grafo: dados/entrada_eulerizada.txt ---
Vértices: 6, Arestas: 10
Graus dos vértices:
Vértice | In-Degree | Out-Degree | Status
--------|-----------|------------|-------
   0    |     1     |      1     | OK
   1    |     2     |      2     | OK
   2    |     2     |      2     | OK
   3    |     1     |      1     | OK
   4    |     2     |      2     | OK
   5    |     2     |      2     | OK
Circuito Euleriano encontrado:
a -> c -> b -> f -> c -> e -> f -> e -> d -> b -> a
Custo Total do Circuito: 10
```

O programa identificou corretamente que o grafo está balanceado e encontrou um circuito euleriano com um custo total de 10. O circuito encontrado é `a -> c -> b -> f -> c -> e -> f -> e -> d -> b -> a`.

## 5. Conclusão

O trabalho demonstrou a aplicação dos conceitos de modelagem de dígrafos ponderados, cálculo de graus de entrada e saída, identificação de vértices desbalanceados e eulerização manual. A implementação do algoritmo de Hierholzer em Python foi bem-sucedida na identificação de um circuito euleriano e seu custo total em um grafo eulerizado. Os resultados obtidos estão de acordo com as expectativas para um grafo euleriano com as arestas e pesos definidos.

## 6. Arquivos Entregues

-   `hierholzer.py`: Implementação do algoritmo de Hierholzer.
-   `dados/entrada_original.txt`: Grafo oficial original.
-   `dados/entrada_eulerizada.txt`: Grafo oficial eulerizado.
-   `dados/entrada_exemplo.txt`: Grafo de exemplo fornecido pelo usuário (não eulerizado).
-   `dados/entrada_exemplo_eulerizada.txt`: Grafo de exemplo eulerizado fornecido pelo usuário.
-   `relatorio_carteiro_chines.md`: Este relatório.
