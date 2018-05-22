num_of_c = float(0)  # number of nodes that are cooperation
num_of_nodes = float(0)  # number of nodes that are in given graph
alpha = float(0.1)  # learning rate
eps = 0.1  # greedy - exploration or exploitation
gamma = 0.6  # discount factor, determines the importance of future rewards. Close to 1, it may diverge
q_function = []  # the first index refers to cooperation,
# the second refers to defection.
strategy = ["C", "D"]  # strategy set

inter_info_list = [] # List of instance of myNodeInfo. Each item in the list contains intermediate information 
# for corresponding node when doing each iteration of learning. This information is specifcally used to judge whether or 
# the learning method is correct.
content = '' # total intermediate information 

class myNodeInfo: # Each instance includes the intermediate information
    def __init__(self, id, ran_num=0.00, ex_or_ex='None', sel_str='C', payoff=0, new_val_table={'C': 0, 'D': 0}):
        self.id = str(id)
        self.ran_num = str('{0:.2f}'.format(ran_num))
        self.ex_or_ex = ex_or_ex
        self.sel_str = sel_str
        self.payoff = str(payoff)
        self.new_val_table = new_val_table
    
    def description(self):
        len_id = len(str(num_of_nodes))
        str_table = '[C: %.2f, D: %.2f]' %(self.new_val_table['C'], self.new_val_table['D'])
        # des_str = "Node %f, random num: %.2f, %s, %s, payoff: %.2f, %f." % (
        #     self.id, self.ran_num, self.ex_or_ex, self.sel_str, self.payoff, self.id) 
        des_str = 'node ' + (len_id - len(self.id)) * ' ' + self.id + ', random: ' + self.ran_num + ', ' + self.ex_or_ex \
          + (12 - len(self.ex_or_ex)) * ' ' + ', ' + self.sel_str + ', payoff: ' + self.payoff + ', current q table: ' + str_table
        return des_str