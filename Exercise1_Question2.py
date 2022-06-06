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


#########################################################
# The function gets as a parameter n - the motif's size #
# Returns list of all motifs with size n                #
#########################################################
def create_motifs_list_from_txt_file(n):
    # Checking that the txt file with all motifs of size n exists in directory
    try:
        motifs_file = open(f'sub_graphs_with_{n}_nodes.txt', 'r')
    except FileNotFoundError:
        raise Exception(f"\n\n#######################################################################"
                        f"\n### File: \"sub_graphs_with_{n}_nodes.txt\" doesn\'t exist in directory! ###"
                        f"\n### Please run Exercise1.py with n=4 to produce the motifs file!    ###"
                        f"\n#######################################################################")

    lines = motifs_file.readlines()  # Reading all lines from txt file
    row_num = 0
    motif = []
    motifs_list = []
    matches = ["n", "count", "#"]
    for line in lines:
        if not any(match in line for match in matches):
            # Creating new edge and appending to motif's edges
            motif.append(tuple([int(val) for val in line.replace('\n', '').split(" ")]))
        else:
            # Finished creating the motif, appending to general list of motifs with size "n"
            if row_num >= 3:
                motifs_list.append(motif)
                motif = []
        row_num += 1

    # Append the last motif to the list
    motifs_list.append(motif)
    return motifs_list


################################################################
# The function gets as a parameter the graph's edges file path #
# Returns a list of edges created from the txt file            #
################################################################
def create_graph_from_edges_list_file(edges_list_file_path):
    try:
        edges_list_file = open(edges_list_file_path, 'r')
    except FileNotFoundError:
        print_str = f'### File: \"{edges_list_file_path}\" doesn\'t exist in directory! ###'
        second_line = f'### Please enter the correct file\'s path!'
        raise Exception(f"\n\n" + "#" * len(print_str) +
                        f"\n### File: \"{edges_list_file_path}\" doesn\'t exist in directory! ###"
                        f"\n" + second_line + " " * (len(print_str) - len(second_line) - 3) + "###"
                                                                                              f"\n" + "#" * len(
            print_str))

    graph_edges = []
    for line in edges_list_file.readlines():
        graph_edges.append(tuple([int(val) for val in line.replace('\n', '').split(" ")]))
    return graph_edges


#########################################################################
# Function that gets as input a motif and a graph.                      #
# Returns the number of sub-graphs isomorphic to the motif in the graph #
#########################################################################
def sub_graphs_isomorphism_count(motif, test_graph_edges):
    # checking if the number of edges in the
    # motif exceed number of edges in the test graph.
    # If True, no chance of isomorphic sub-graph existence
    # in the given graph.
    if len(motif) > len(test_graph_edges):
        return 0
    all_combinations_edges_test_graph = [list(comb) for comb in combinations(test_graph_edges, len(motif))]

    count_isomorphic = 0
    for comb in all_combinations_edges_test_graph:
        G1 = nx.DiGraph()
        G2 = nx.DiGraph()

        G1.add_edges_from(motif)
        G2.add_edges_from(comb)
        if nx.is_isomorphic(G1, G2):
            count_isomorphic += 1

    return count_isomorphic

########
# Main #
########
if __name__ == "__main__":
    #TODO: ################################### REMOVE BEFORE HAND IN!!! ################################
    n = int(input("Please insert n (Number of vertices in sub-graphs) --> "))
    edges_list_file_path = input("Please enter path to txt file with edges for the given graph --> ")
    # n = 4
    # edges_list_file_path = 'edges_list.txt'
    ##############################################################################################

    # Converting txt file to motifs edge list representation
    all_motifs_list = create_motifs_list_from_txt_file(n)

    # Converting given file to a given graph in the format:
    # test_graph = [e1, e2, ..., ek] = [(v1, v2), (v1', v2'), ...,]
    test_graph_edges = create_graph_from_edges_list_file(edges_list_file_path)

    # Getting number of sub-graphs isomorphic to each motif in the given graph
    motif_count = [0 for i in range(len(all_motifs_list))]
    for motif_idx, motif in enumerate(all_motifs_list):
        motif_count[motif_idx] = sub_graphs_isomorphism_count(motif, test_graph_edges)

    # Creating txt file with count of all sub-graphs that are isomorphic to the motifs
    # in a given graph, denoted by the set of edges taken from a txt file: "edges_list.txt"
    with open(f'sub_graphs_isomorphic_count_with_{n}_nodes_tmp.txt', 'w') as motif_count_file:
        motif_count_file.writelines([f"graph={test_graph_edges}\n"])
        motif_count_file.writelines([f"n={n}\n\n"])
        for idx, count in enumerate(motif_count):
            lines = [f"#{idx+1}\n", f"motif={all_motifs_list[idx]}\n", f"count={count}\n"]
            motif_count_file.writelines(lines)
            print(f"#{idx + 1}\n"
                  f"motif={all_motifs_list[idx]}\n"
                  f"count={count}\n")
    print(f"Successfully created \"sub_graphs_isomorphic_count_with_{n}_nodes.txt\" file!")