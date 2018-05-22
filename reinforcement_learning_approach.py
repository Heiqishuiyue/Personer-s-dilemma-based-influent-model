import config
import random
import graph_based_functions as gbf
import graph_models
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

def arg_max(q_list):
    """
    return the max strategy
    :param q_list: q value for a node
    :return: the strategy either cooperation or cooperation
    """
    expected_value_c = q_list["C"]
    expected_value_d = q_list["D"]
    if expected_value_c > expected_value_d:
        return "C"
    elif expected_value_c < expected_value_d:
        return "D"
    else:
        return config.strategy[random.randint(0, 1)]


def max_q_value(q_list):
    """
    return the largest expected value
    :param q_list: a dictionary for strategy - value items
    :return: the largest expected value
    """
    expected_value_c = q_list["C"]
    expected_value_d = q_list["D"]
    if expected_value_c >= expected_value_d:
        return expected_value_c
    elif expected_value_c < expected_value_d:
        return expected_value_d


def update_q_value(i, nodes):
    """
    update expected value(Q value) for given node
    :param i: the id of given node
    :param nodes: nodes list for given graph
    :return: none
    """
    current_node = nodes[i]
    config.q_function[i][current_node["Strategy"]] += config.alpha * (float(current_node["Payoff"]) +
                config.gamma * max_q_value(config.q_function[i]) - config.q_function[i][current_node["Strategy"]])


def learning(graph):
    nodes = graph.nodes()
    for i in nodes:
        if not nodes[i]["IsSeed"]:
            random_number = random.uniform(0, 1)
            print(random_number)
            if random_number < config.eps:  # exploration
                selected_strategy = config.strategy[random.randint(0, 1)]
                nodes[i]["Strategy"] = selected_strategy
                ex_or_ex = 'exploration'
            else:  # exploitation
                selected_strategy = arg_max(config.q_function[i])
                nodes[i]["Strategy"] = selected_strategy
                ex_or_ex = 'exploitation'
            config.inter_info_list.append(config.myNodeInfo(i, random_number, ex_or_ex, selected_strategy))   
        else:
            config.inter_info_list.append(config.myNodeInfo(i))    
    gbf.play_game(graph)
    nodes = graph.nodes()
    index = 0
    for i in nodes:
        if not nodes[i]["IsSeed"]:
            update_q_value(i, nodes)
        # append intermediate information to config.content 
        cur_node_info = config.inter_info_list[index]
        cur_node_info.payoff = nodes[i]['Payoff']
        cur_node_info.new_val_table = config.q_function[i]
        index += 1
    config.content += get_inter_info_form_list(config.inter_info_list) + '\n' + '\n'
    config.inter_info_list.clear()


def color_and_show_graph(graph):
    color_map = graph_models.set_colors_to_nodes(graph)
    nx.draw(graph, node_color=color_map, with_labels=True)
    plt.show()


def log_info_import():
    # file name will be appended with the output daytime
    fileName = "Re_learning_inter_info_" + str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".txt"
    output_file = open(fileName, "w")
    output_file.write(config.content)
    output_file.close()


def get_inter_info_form_list(list):
    content = ''
    for node in config.inter_info_list:
        content += node.description() + '\n'
    return content

def main():
    # new_graph = gbf.import_graph_from_txt('dolphins.txt')
    new_graph = gbf.import_graph_from_txt('simple_graph.txt')
    # new_graph = nx.watts_strogatz_graph(100, 7, 0.3, seed=5)
    # new_graph = nx.erdos_renyi_graph(100, 0.1)
    # new_graph = graph_models.get_star_graph(6)
    # new_graph = nx.scale_free_graph(100)
    gbf.init_nodes_with_attributes(new_graph)
    
    most_top_node = gbf.get_n_top_degree_node(new_graph, 3)
    gbf.set_seeds(most_top_node, new_graph)
    gbf.print_nodes_information(new_graph)
    for _ in range(1000):
        learning(new_graph)
    gbf.print_nodes_information(new_graph)
    print(config.q_function)
    print("Number of c:" + str(gbf.get_number_of_c(new_graph)))
    log_info_import()
    # color_and_show_graph(new_graph)
    
   

main()

