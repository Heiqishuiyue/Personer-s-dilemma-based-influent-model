payoff_table = {('D', 'D'): 0, ('D', 'C'): 1.2, ('C', 'D'): 0, ('C', 'C'): 1}
beta = 1.2


def get_payoff(my_strategy, the_other_strategy):
    return payoff_table[(my_strategy, the_other_strategy)]

