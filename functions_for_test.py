import graph_based_functions as gf
import data_visualisation as vis
import config


def turn_nodes_to_specified_strategy(nodes_list, strategy, graph):
    nodes = graph.nodes()
    for i in nodes_list:
        nodes[i]['Strategy'] = strategy


def get_n_top_influential_nodes(graph, top_degree_node_id_list, num_of_nodes=3):
    """
    A greedy way to seek the most influential nodes
    :param graph:
    :param top_degree_node_id_list:
    :param num_of_nodes:
    :return:
    """
    nodes = graph.nodes()
    clone_nodes = list(nodes)
    rate_dict = {}
    for id in top_degree_node_id_list:
        del clone_nodes[id]
    seed_set = top_degree_node_id_list
    rate_node = {0: float(0)}
    for n in range(2, num_of_nodes):
        gf.set_seeds(seed_set, graph)
        for i in clone_nodes:
            nodes[i]['IsSeed'] = True
            nodes[i]['Strategy'] = 'C'
            for j in range(0, 100):
                gf.play_game(graph)
                gf.update_strategy(gf.judge_current_strategy(graph), graph)
            new_rate = config.num_of_c / config.num_of_nodes
            rate_dict[i] = new_rate
            print(new_rate)
            if new_rate > list(rate_node.values())[0]:
                rate_node.clear()
                rate_node = {i: new_rate}
            gf.init_nodes_with_attributes(graph)
            gf.set_seeds(seed_set, graph)
        seed_set.append(list(rate_node.keys())[0])

        del clone_nodes[list(rate_node.keys())[0]]
    print(rate_dict)
    vis.vis_rate_for_nodes(rate_dict)
    return seed_set


# def main():
#     new_graph = gf.import_graph_from_txt('dolphins.txt')
#     gf.init_nodes_with_attributes(new_graph)
#     gf.print_nodes_information(new_graph)
#     most_top_node = gf.get_n_top_degree_node(new_graph, 2)
#     seed_set = get_n_top_influential_nodes(new_graph, most_top_node)
#     print(seed_set)
# if __name__ == '__main__':
#     main()
