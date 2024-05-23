import networkx as nx

def christofides_rpp(G):
    # Create a minimum spanning tree of the graph
    MST = nx.minimum_spanning_tree(G)

    # Identify the set of odd-degree vertices in the MST
    odd_vertices = [v for v in MST.nodes() if MST.degree(v) % 2 == 1]

    # Create a minimum weight perfect matching on the set of odd-degree vertices
    matching = nx.bipartite.minimum_weight_full_matching(G, odd_vertices)

    # Combine the MST and the minimum weight perfect matching to form a multi-graph
    multi_graph = nx.MultiGraph(MST)
    for u, v, weight in matching:
        multi_graph.add_edge(u, v, weight=weight)

    # Find an Eulerian tour of the multi-graph
    tour = nx.eulerian_circuit(multi_graph)

    # Convert the Eulerian tour into a Hamiltonian cycle by removing any repeated vertices
    hamiltonian_cycle = []
    for u, v in tour:
        if u not in hamiltonian_cycle:
            hamiltonian_cycle.append(u)
        if v not in hamiltonian_cycle:
            hamiltonian_cycle.append(v)

    return hamiltonian_cycle