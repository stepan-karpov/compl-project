import networkx as nx

from main import christofides_rpp

def test_rpp():
    # Test 1: Trivial case with one vertex and no edges
    G = nx.Graph()
    G.add_node(1)
    solution = christofides_rpp(G)
    assert solution == [1], f"Expected [1] but got {solution}"

    # Test 2: Trivial case with two vertices and one edge
    G = nx.Graph()
    G.add_edge(1, 2, weight=1)
    solution = christofides_rpp(G)
    assert solution == [1, 2, 1], f"Expected [1, 2, 1] but got {solution}"

    # Test 3: Simple case with three vertices and three edges
    G = nx.Graph()
    G.add_edge(1, 2, weight=1)
    G.add_edge(2, 3, weight=2)
    G.add_edge(3, 1, weight=3)
    solution = christofides_rpp(G)
    assert solution == [1, 2, 3, 1], f"Expected [1, 2, 3, 1] but got {solution}"

    # Test 4: Complex case with four vertices and six edges
    G = nx.Graph()
    G.add_edge(1, 2, weight=1)
    G.add_edge(2, 3, weight=2)
    G.add_edge(3, 4, weight=3)
    G.add_edge(4, 1, weight=4)
    G.add_edge(1, 3, weight=5)
    G.add_edge(2, 4, weight=6)
    solution = christofides_rpp(G)
    assert solution == [1, 2, 3, 4, 1], f"Expected [1, 2, 3, 4, 1] but got {solution}"