#####################################
# Biological Computing - Exercise 1 #
#       Roy Assa 322542226          #
#       Itav Nissim 322713488       #
#           20/05/2022              #
#####################################


###########
# Imports #
###########
import networkx as nx
from itertools import combinations
import numpy as np


############################################################################
# The function checks for connectivity in combinations (sub-graphs).       #
# In addition, it checks if there exists isomorphic sub-graph.             #
# If exists any, it keeps in the list a single instance of the             #
# isomorphic sub-graphs.                                                   #
# The Function returns all combinations satisfying the above restrictions. #
############################################################################
def iSubset(arr, size):
    combinations_lst_size_i = [list(comb) for comb in combinations(arr, size) if check_connectivity(comb) is True]
    connected_non_isomorphic_combination = []
    loop_idx = 0
    while loop_idx < len(combinations_lst_size_i):
        combination = combinations_lst_size_i[loop_idx]
        combinations_lst_size_i = remove_all_isomorphic_sub_graphs(combination, loop_idx, combinations_lst_size_i)
        loop_idx += 1
        connected_non_isomorphic_combination.append(combination)
    return connected_non_isomorphic_combination


#########################################################################
# Function that checks if current combination (sub-graph) is isomorphic #
# to a different combination (sub-graph) in the list                    #
#########################################################################
def remove_all_isomorphic_sub_graphs(comb, comb_index, combinations_lst):
    curr_idx = 0
    while curr_idx < len(combinations_lst):
        curr_comb = combinations_lst[curr_idx]
        if curr_comb:
            if curr_idx != comb_index:
                G1 = nx.DiGraph()
                G1.add_edges_from(comb)
                G2 = nx.DiGraph()
                G2.add_edges_from(curr_comb)

                # Checking if current sub-graphs are isomorphic
                if nx.is_isomorphic(G1, G2):
                    combinations_lst[curr_idx] = []  # Place a dummy
        curr_idx += 1

    return [c for c in combinations_lst if c != []]  # Remove dummies


########################################################################
# Function that checks if current combination (sub-graph) is connected #
########################################################################
def check_connectivity1(graph):
    vertex_count = [0 for index in range(n)]  # vertices list: [0, 1, ..., n-1]

    for edge in graph:  # [v1, v2]
        v1 = edge[0]
        v2 = edge[1]
        vertex_count[v1] += 1
        vertex_count[v2] += 1

    # Checking if the current combination (sub-graph) is connected
    # using list of appearances for vertices in the edges
    if np.sum([count == 0 for count in vertex_count]) >= 1:
        print("#####################################")
        print("# The following graph is not connected:")
        print(graph)
        print("#####################################")
        return False

    return True


########################################################################
# Function that checks if current combination (sub-graph) is connected #
########################################################################
def check_connectivity(combination):
    G = nx.DiGraph()
    G.add_edges_from(combination)
    G_undirected = G.to_undirected()

    if nx.is_connected(G_undirected):
        return check_connectivity1(combination)
    return False


###################################################
# Function that writes to txt file all sub-graphs #
###################################################
def write_to_txt_file(all_sub_graphs_list, n, count):
    """
    # Function that writes to txt file all the sub-graphs in the following format:
      n=_
      count=_
      #1
      v1, v2
      v1', v2'
      ...
      #k
      v1'', v2''
    """
    with open(f'sub_graphs_with_{n}_nodes.txt', 'w') as f:
        f.write(f'n={n}\n')
        f.write(f"count={count}\n")
        motif = 1
        for sub_graphs_lst_size_i in all_sub_graphs_list:  # Running on all lists of sub-graphs of all sizes
            for sub_graph in sub_graphs_lst_size_i:  # Running on all sub-graphs of a given size
                f.write(f"#{motif}\n")
                for edge in sub_graph:  # Running on all edges in a single sub-graph
                    f.write(f"{edge[0] + 1} {edge[1] + 1}\n")  # Writing a specific edge to txt file
                motif += 1


########
# Main #
########
if __name__ == "__main__":
    n = int(input("Please insert n (Number of vertices in sub-graphs) --> "))

    if n == 1:
        edges_list = [(0, 0)]
        count = 1
        lines = [f"n={n}", f"count={count}", "1 1"]
        with open(f'sub_graphs_with_{n}_nodes.txt', 'w') as f:
            f.write('\n'.join(lines))
        print("count=" + str(count))
    else:
        ######################################################################
        # Part 1: Finding all edges between n vertices in a single sub-graph #
        ######################################################################
        print("##########")
        print("# Part 1 #")
        print("##########")
        print("n = " + str(n))
        G = nx.complete_graph(n, nx.DiGraph())
        edges_list = G.edges
        print("Edges list: {}".format(edges_list), '\n')

        #####################################################################
        # Part 2: Finding all combinations of sizes {n-1, n, ..., n**2 - n} #
        #####################################################################
        print("##########")
        print("# Part 2 #")
        print("##########")
        all_combinations_list = []
        for i in range(n - 1, n ** 2 - n + 1):
            combinations_size_i = iSubset(edges_list, size=i)  # Getting all connected sub-graphs of size i
            all_combinations_list.append(combinations_size_i)
        print("\n")

        # Checking that the number of combinations has been successfully
        # updated for combinations that are not connected.
        # Example: for n=3, we need to take out some combinations where
        # the number of edges is 2 since they can be not connected.
        # (see PDF for further details)
        i = n - 1
        for combinations_lst_size_i in all_combinations_list:
            print("Size of combinations list of size = " + str(i) + " is: " + str(len(combinations_lst_size_i)))
            i += 1
        print("")

        # Printing all sub-graphs found (connected && non-isomorphic)
        count = 1  # numerical index for combination
        i = n - 1  # size of combinations
        for idx, combination_lst_size_i in enumerate(all_combinations_list):
            print("##################################################")
            print("# Sub-graphs of with {} edges are the following: #".format(i))
            print("##################################################")
            i += 1
            for comb in combination_lst_size_i:
                print("Sub-graph #{} is: {}".format(count, comb))
                count += 1
            print("")

        ###########################################################
        # Part 3: Writing to txt file all sub-graphs with n nodes #
        ###########################################################
        print("##########")
        print("# Part 3 #")
        print("##########")
        # Writing all sub-graphs to txt file as instructed
        write_to_txt_file(all_combinations_list, n, count - 1)
        print(f"Successfully wrote to: \"sub_graphs_with_{n}_nodes.txt\"")
        print("count=" + str(count - 1))
