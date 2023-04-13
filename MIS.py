"""
To find Maximum Independent Set v 1.0

Student: Leonid Chernov
Scientific director: Professor Carmine Cerrone
"""

# Firstly we should add two modules
# Networkx is a graph implementation
import networkx as nx
# Matplotlib is a library for creating visualizations in Python
import matplotlib.pyplot as plt

# We create a recursive function that solves the problem of finding Maximum Independent Set
# Below there are two functions 'if' to stop a recursion
#
def sets_of_graph(graph):
    if not graph: # We also can write len(graph) == 0
        return [] # If we have no vertexes it is impossible to solve the problem
    if len(graph) == 1:
        return list(graph.nodes) # Nodes are vertexes. We should represent vertexes in a python list
    actual_vertex = list(graph.nodes)[0] # To take the first vertex from our graph

# We have to remove vertexes from the graph to proceed enumeration
    graph_copy_for_repeat = graph.copy() # We should to copy a graph to repeat the search
    graph_copy_for_repeat.remove_node(actual_vertex) # To remove a vertex

    solution_one = sets_of_graph(graph_copy_for_repeat) # A recursive call to find MIS

    for neighbors in graph.neighbors(actual_vertex): # Enumeration of neighbors (agile vertexes of an actual vertex)
        graph_copy_for_repeat.remove_node(neighbors) # If we find a neighbor a program removes it
# This vertex is not a part of MIS

# Concatenation
# The list of vertexes + MIS of the graph from which we have removed the actual vertex and its neighbors
    solution_two = [actual_vertex] + sets_of_graph(graph_copy_for_repeat)
# We search the lengthiest list, where are the biggest number of vertexes
    return max(solution_one, solution_two, key=len)
# The result of the function is the list

# The main function elaborating the text file, applying all functions for the graph
# To derive the result
#


# We have a text file, where edges of the grath are written
# Now we should open this file in this program in correct way
#
def get_list_edges(take_file):
    with open(take_file) as file: # Although we can work without 'with', albeit in that case we should close file
        list_edges = [] # To create a list for edges
        for line in file:
            line = line.rstrip() # To delete odd symbols in the text
            split_values = line.split() # To create delimiters from whitespaces
            list_edges.append(split_values) # To add the numbers to a list
    return list_edges # To convert the numbers from the text to a python list

# Visualisation of the graph with instruments of Matplotlib
#
def draw_graph(graph, max_independent_set):
    node_color = [
        'green' if node in max_independent_set else 'grey' # Painting the nodes
    for node in graph
    ]
    nx.draw( # To draw the graph
    graph,
    with_labels=True,
    font_weight='bold',
    node_color=node_color,
    )
    plt.show() # To display a figure of the graph
def main():
    take_file = 'body_graph.txt' # To make a variable for the text file
    list_edges = get_list_edges(take_file) # It is the function for adaptation of the text file
    extraction_graph_from_file = nx.Graph() # To create a graph 
    extraction_graph_from_file.add_edges_from(list_edges) # To add the edges from the text file
    maximal_independent_set = sets_of_graph(extraction_graph_from_file)

    draw_graph(extraction_graph_from_file, maximal_independent_set) #To call the function for MIS

    print('The dimension of the graph is ', len(maximal_independent_set))
    print('Vertexes: ', maximal_independent_set)

# To add all function calls and output information on the standard output stream
if __name__ == '__main__':
    main()