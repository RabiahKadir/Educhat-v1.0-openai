import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt

def visualizeRDFTriple(file, _format):
    graph = rdflib.Graph()
    _triple = graph.parse(file, format=_format)
    _graph = rdflib_to_networkx_multidigraph(_triple)
    
    # Plot Networkx instance of RDF Graph
    pos = nx.spring_layout(_graph, scale=2)
    edge_labels = nx.get_edge_attributes(_graph, 'r')
    nx.draw_networkx_edge_labels(_graph, pos, edge_labels=edge_labels)
    nx.draw(_graph, with_labels=True)
    plt.show()
