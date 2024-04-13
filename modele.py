import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)])

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
# Create a similarity matrix
similarity_matrix = np.zeros((10, 10))

# Fill the similarity matrix with random values
for i in range(10):
    for j in range(10):
        similarity_matrix[i, j] = np.random.rand()

# 3. Initialisation des clusters

# Initialiser les clusters
clusters = {
    0: [1, 2, 3],
    1: [4, 5, 6],
    2: [7, 8, 9, 10]
}

# 4. Calcul de la connectivité des clusters

# Calculer la connectivité de chaque cluster
cluster_connectivities = {}
for cluster_id, nodes in clusters.items():
    cluster_connectivities[cluster_id] = nx.average_clustering(G, nodes)

# 5. Calcul de la probabilité d'homogénéité

# Calculer la probabilité d'homogénéité pour chaque cluster
cluster_probabilities = {}
for cluster_id, nodes in clusters.items():
    cluster_probabilities[cluster_id] = 1
    for node in nodes:
        cluster_probabilities[cluster_id] *= similarity_matrix[node - 1, node - 1]

# 6. Application des règles

# Appliquer les règles pour déterminer l'appartenance des nouveaux utilisateurs
new_user = 11

# Règle 1 : Bon ajustement
if cluster_probabilities[0] > cluster_probabilities[1] and cluster_probabilities[0] > cluster_probabilities[2]:
    clusters[0].append(new_user)
elif cluster_probabilities[1] > cluster_probabilities[0] and cluster_probabilities[1] > cluster_probabilities[2]:
    clusters[1].append(new_user)
else:
    clusters[2].append(new_user)

# Règle 2 : Mauvais ajustement
if cluster_probabilities[0] < cluster_probabilities[1] and cluster_probabilities[0] < cluster_probabilities[2]:
    if new_user in clusters[0]:
        clusters[0].remove(new_user)
elif cluster_probabilities[1] < cluster_probabilities[0] and cluster_probabilities[1] < cluster_probabilities[2]:
    if new_user in clusters[1]:
        clusters[1].remove(new_user)

else:
    if new_user in clusters[2]:
        clusters[2].remove(new_user)

# Résultats attendus :

# Afficher les clusters résultants
print(clusters)
