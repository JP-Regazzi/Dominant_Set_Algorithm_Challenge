import sys, os, time
import networkx as nx

def dominant(graph):
    """
        A Faire:
        - Ecrire une fonction qui retourne deux dominants du graphe non dirigé g passé en parametre.
        - Cette fonction doit retourner une liste contenant deux sous-listes. Les sous-listes sont les noeuds des dominants D1 et D2.
        - Le score est (|D1| + |D2| + |D1 inter D2|) / |V|, où |V| est le nombre de noeuds du graphe.
        - Ce score doit être minimal.
        - La pondération des sommets n'a pas d'importance pour le calcul du score.

        :param g: le graphe est donné dans le format networkx : https://networkx.github.io/documentation/stable/reference/classes/graph.html

    """

    def get_longest_path(graph):
        def dfs(node, visited, path):
            visited.add(node)
            path.append(node)
            longest = path.copy()

            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    current_path = dfs(neighbor, visited, path)
                    if len(current_path) > len(longest):
                        longest = current_path

            path.pop()
            visited.remove(node)
            return longest

        longest_path = []
        for node in graph.nodes():
            current_path = dfs(node, set(), [])
            if len(current_path) > len(longest_path):
                longest_path = current_path
        return longest_path
    
    def generate_dom_set1(start_node, graph):
        dom_set1 = []
        temp_graph = graph.copy()

        while temp_graph.nodes():
            dom_set1.append(start_node)
            for neighbor in list(temp_graph.neighbors(start_node)):
                temp_graph.remove_node(neighbor)
            temp_graph.remove_node(start_node)
            if temp_graph.nodes():
                start_node = max(temp_graph.degree, key=lambda x: x[1])[0]
        return dom_set1

    def generate_dom_set2(start_node, graph, dom_set1):
        dom_set2 = [start_node]
        temp_graph = graph.copy()
        for neighbor in list(temp_graph.neighbors(start_node)):
            temp_graph.remove_node(neighbor)
        temp_graph.remove_node(start_node)

        while temp_graph.nodes():
            nodes_excluding_dom_set1 = [n for n in temp_graph.nodes() if n not in dom_set1]
            if nodes_excluding_dom_set1:
                max_node = max(nodes_excluding_dom_set1, key=lambda n: temp_graph.degree(n))
            else:
                max_node = max(temp_graph.degree, key=lambda x: x[1])[0]
            dom_set2.append(max_node)
            for neighbor in list(temp_graph.neighbors(max_node)):
                temp_graph.remove_node(neighbor)
            temp_graph.remove_node(max_node)
        return dom_set2
    
    def compute_score(set1, set2, graph):
        intersection_size = len(set(set1) & set(set2))
        total_nodes = len(set1) + len(set2) + intersection_size
        return total_nodes / len(graph.nodes())

    def is_dominating_set(graph, dom_set):
        for node in graph.nodes():
            if node not in dom_set and not any(neighbor in dom_set for neighbor in graph.neighbors(node)):
                return False
        return True

    # Special case handling
    if len(graph.nodes()) == len(graph.edges()):
        # Get the longest path in graph
        longest_path = get_longest_path(graph)
        # Split nodes in the longest path into dom_set1 and dom_set2
        dom_set1 = [longest_path[i] for i in range(0, len(longest_path), 3)]
        dom_set2 = [longest_path[i] for i in range(1, len(longest_path), 3)]
        if longest_path[-1] not in dom_set2:
            dom_set2.append(longest_path[-1])
        if is_dominating_set(graph, dom_set1) and is_dominating_set(graph, dom_set2):
            return [dom_set1, dom_set2]

    dom_set1_trials = []
    top_degree_nodes = sorted(graph.degree, key=lambda x: x[1], reverse=True)[:25]
    for node, _ in top_degree_nodes:
        dom_set1_trials.append(generate_dom_set1(node, graph))

    dom_set1 = min(dom_set1_trials, key=lambda x: len(x))

    temp_graph = graph.copy()
    temp_graph.remove_nodes_from(dom_set1)
    top_degree_nodes = sorted(temp_graph.degree, key=lambda x: x[1], reverse=True)[:25]
    dom_set2_trials = []
    for node, _ in top_degree_nodes:
        dom_set2_trials.append(generate_dom_set2(node, graph, dom_set1))

    best_score = float('inf')
    for trial in dom_set2_trials:
        score = compute_score(dom_set1, trial, graph)
        if score < best_score:
            dom_set2 = trial
            best_score = score

    return [dom_set1, dom_set2]

    # weights = nx.get_node_attributes(g, 'weight')   # Pour obtenir un itérable avec les poids.
    # return list(g.nodes), list(g.nodes)  # Une solution, c'est la plus mauvaise possible, score de 1.


#########################################
#### Ne pas modifier le code suivant ####
#########################################


def load_graph(name):
    with open(name, "r") as f:
        state = 0
        G = None
        for l in f:
            if state == 0:  # Header nb of nodes
                state = 1
            elif state == 1:  # Nb of nodes
                nodes = int(l)
                state = 2
            elif state == 2:  # Header position
                i = 0
                state = 3
            elif state == 3:  # Position
                i += 1
                if i >= nodes:
                    state = 4
            elif state == 4:  # Header node weight
                i = 0
                state = 5
                G = nx.Graph()
            elif state == 5:  # Node weight
                G.add_node(i, weight=int(l))
                i += 1
                if i >= nodes:
                    state = 6
            elif state == 6:  # Header edge
                i = 0
                state = 7
            elif state == 7:
                if i > nodes:
                    pass
                else:
                    edges = l.strip().split(" ")
                    for j, w in enumerate(edges):
                        w = int(w)
                        if w == 1 and (not i == j):
                            G.add_edge(i, j)
                    i += 1

        return G


#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__ == "__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])

    # un repertoire des graphes en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
        print(input_dir, "doesn't exist")
        exit()

    # un repertoire pour enregistrer les dominants doit être passé en parametre 2
    if not os.path.isdir(output_dir):
        print(input_dir, "doesn't exist")
        exit()

        # fichier des reponses depose dans le output_dir et annote par date/heure
    output_filename = 'answers_{}.txt'.format(time.strftime("%d%b%Y_%H%M%S", time.localtime()))
    output_file = open(os.path.join(output_dir, output_filename), 'w')

    for graph_filename in sorted(os.listdir(input_dir)):
        # importer le graphe
        g = load_graph(os.path.join(input_dir, graph_filename))

        # calcul du dominant
        d1, d2 = dominant(g)
        D1 = sorted(d1, key=lambda x: int(x))
        D2 = sorted(d2, key=lambda x: int(x))

        # ajout au rapport
        output_file.write(graph_filename)
        for node in D1:
            output_file.write(' {}'.format(node))
        output_file.write('-')
        for node in D2:
            output_file.write(' {}'.format(node))
        output_file.write('\n')

    output_file.close()
