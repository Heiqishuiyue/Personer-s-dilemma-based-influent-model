import networkx as nx
import matplotlib.pyplot as plt
import graph_based_functions as gbf
import functions_for_test as ftest
import config


def get_star_graph(n):
    graph = nx.Graph()
    for i in range(2, n+1):
        graph.add_edge(1, i)
    return graph


def get_path_graph(n):  # get a path graph
    return nx.path_graph(n)


def set_colors_to_nodes(graph):
    color_map = []
    nodes = graph.nodes
    for i in nodes:
        if nodes[i]["Strategy"] == "C":
            color_map.append("yellow")
            config.num_of_c += 1
        else:
            color_map.append("blue")
    return color_map


# def main():
#     graph = get_path_graph(6)
#     gbf.init_nodes_with_attributes(graph)
#     gbf.print_nodes_information(graph)
#     list = [1, 2, 3]
#     ftest.turn_nodes_to_specified_strategy(list, "C", graph)
#     gbf.print_nodes_information(graph)
#     gbf.play_game(graph)
#     print()
#     gbf.print_nodes_information(graph)
#     nx.draw(graph)
#     plt.show()
# main()