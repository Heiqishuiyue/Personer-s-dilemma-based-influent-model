import xlrd
import matplotlib.pyplot as plt
import networkx as nx
import matrix_payoff
import random
import config


def import_graph_from_txt(path):
    """
    return a networkxx graph from a .txt file
    :param path: the path of the file
    :return: a graph
    """
    graph = nx.Graph()
    file = open(path, "r")
    for line in file:
        nodes = line.split()
        graph.add_edge(int(nodes[0]), int(nodes[1]))
    return graph


def init_nodes_with_attributes(graph):
    """
    Set a strategy attribute for every node in graph with a initial value - D (defection)
    :param graph: a networkx graph
    :return:
    """
    nodes = graph.nodes()
    config.num_of_nodes = len(nodes)
    config.q_function = [{"C": float(0), "D": float(0)} for i in range(0, len(nodes) + 1)]
    print(config.num_of_nodes)
    for n in nodes:
        nodes[n]["Strategy"] = "D"
        nodes[n]["Payoff"] = float(0)
        nodes[n]["IsSeed"] = bool(False)
        # print(n, graph.degree(n),nodes[n]["Strategy"])
    config.num_of_c = 0


def print_nodes_information(graph):
    nodes = graph.nodes()
    number_of_nodes = len(nodes)
    for n in nodes:
        print('ID: ' + str(n) + " " * (len(str(number_of_nodes)) - len(str(n))), '| Strategy: ' + nodes[n]['Strategy'],
              '| Payoff: ' + str(nodes[n]['Payoff']), "| neighbours: ", get_neighbors_list(graph, n))
    print()


def get_neighbors_list(graph, node):
    """
    get a neighbour list
    :param graph: A given networkx graph
    :param node: A specific node
    :return: A node list
    """
    neighbors = []
    for n in graph.neighbors(node):
        neighbors.append(n)
    return neighbors


def degree_sorting(graph):
    return sorted(graph.degree, key=lambda x: x[1], reverse=True)


def get_number_of_c(graph):
    count = 0
    nodes = graph.nodes()
    for i in nodes:
        current_node = nodes[i]
        if current_node["Strategy"] == "C":
            count += 1
    return count


def get_n_top_degree_node(graph, n=1):
    """
    Get the node ID with the highest degree
    :param graph: A networkx graph
    :param n: The number of most top node that goes to return
    :return: ID of the node
    """
    dictionary_degree = degree_sorting(graph)
    key_list = []
    for value in dictionary_degree:
        key_list.append(value[0])
    return key_list[0:n]


def set_seeds(node_id_list, graph):
    node_list = graph.nodes()
    for i in node_id_list:
        node_list[i]['Strategy'] = 'C'
        node_list[i]['IsSeed'] = True
    config.num_of_c = len(node_id_list)


########################################################################################################################
def play_game(graph):
    """
    Each node plays PDG with its neighbours and update its payoff
    :param graph:
    :return:
    """
    nodes = graph.nodes()
    for n in nodes:
        current_node = nodes[n]
        neighbours_index = get_neighbors_list(graph, n)
        total_payoff = 0
        for n_1 in neighbours_index:
            current_neighbour = nodes[n_1]
            total_payoff += matrix_payoff.get_payoff(current_node['Strategy'], current_neighbour['Strategy'])
        current_node['Payoff'] = "{0:.1f}".format(total_payoff)


def judge_current_strategy(graph):
    """
    Each node play PDG with its adjacent nodes and update the potential new strategy
    :param graph: A networkx graph
    :return: A dictionary that contains new strategy for each node
    """
    nodes = graph.nodes()
    new_value_dictionary = {-1: "D"}
    for n in nodes:
        print("ID: " + str(n))
        current_node = nodes[n]
        neighbours = get_neighbors_list(graph, n)
        random_neighbour_index = neighbours[random.randint(0, len(neighbours) - 1)]
        random_neighbour = nodes[random_neighbour_index]
        payoff = float(current_node['Payoff'])
        new_payoff = float(random_neighbour['Payoff'])
        print(not current_node["IsSeed"])
        if new_payoff > payoff and (not current_node["IsSeed"]) and \
                current_node['Strategy'] != random_neighbour['Strategy']:
            print("In in")
            new_length = len(get_neighbors_list(graph, random_neighbour_index))
            probability = (new_payoff - payoff)/(new_length * 1.2)
            print("Probability: " + str(probability))
            random_number = random.uniform(0, 1)
            print("Random number: " + str(random_number))
            if random_number < probability:
                new_value_dictionary[n] = random_neighbour['Strategy']
                if random_neighbour['Strategy'] == 'C':
                    config.num_of_c += 1
                else:
                    config.num_of_c -= 1
            else:
                new_value_dictionary[n] = current_node['Strategy']
        else:
            new_value_dictionary[n] = current_node['Strategy']
    return new_value_dictionary


def update_strategy(strategy_dictionary, graph):
    nodes = graph.nodes()
    for n in nodes:
        current_node = nodes[n]
        current_node['Strategy'] = strategy_dictionary[n]
########################################################################################################################


# def main():
#     rate_node = {0: float(0)}
#     print(type(rate_node.values()))
#
# main()