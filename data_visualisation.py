import numpy as np
import matplotlib.pyplot as plt


def vis_rate_for_nodes(dict):
    keys = []
    values = []
    for key, value in dict.items():
        keys.append(key)
        values.append(value)
    objects = keys
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Rate')
    plt.title('Node')
    plt.show()


# def main():
#     objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
#     y_pos = np.arange(len(objects))
#     performance = [10, 8, 6, 4, 2, 1]
#
#     plt.bar(y_pos, performance, align='center', alpha=0.5)
#     plt.xticks(y_pos, objects)
#     plt.ylabel('Usage')
#     plt.title('Programming language usage')
#
#     plt.show()
#
# main()