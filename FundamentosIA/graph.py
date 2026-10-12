import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

matriz_adjacencia = np.array(
    [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
)

graph = nx.from_numpy_array(matriz_adjacencia)
graph.add_edge(0, 3)  # Adicionando uma aresta entre os nós 0 e 3

mapping = {i: l for i, l in enumerate([
    'A', 'B', 'C', 'D'
])}

graph = nx.relabel_nodes(graph, mapping)


nx.draw(graph, with_labels=True, node_color='black', node_size=800, font_weight='bold')
plt.show()
