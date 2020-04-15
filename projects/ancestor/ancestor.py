from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    #Create a graph
    graph = Graph()
    #For each item in ancestors, add ther vertexs and then the edge between them
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])

    #Create a queue like in a bfs
    queue = Queue()
    #Add to the queue the starting node 
    queue.enqueue([starting_node])


    max_path_length = 1
    #Set an earliest ancestor (defualt:-1)
    earliest_ancestor = -1

    #While the queue size is greater than zero
    while queue.size() > 0:
        #add to the path the dequeued item
        path = queue.dequeue()
        #Set the current node = to the last item in path
        current_node = path[-1]

        #Check which parent is smaller, and if the path is longer
        smaller_value = (len(path) == max_path_length and current_node < earliest_ancestor)

        #Check if the path is longer
        longer_path = (len(path) >  max_path_length)

        #IF either of those are true
        if smaller_value or longer_path:
            #Set the earliest ancestor to the current_node
            earliest_ancestor = current_node
            #Set the max path  length to the length of the current path
            max_path_length = len(path)

        #For each parent of the current node
        for parent in graph.vertices[current_node]:
            #Create a copy of the path
            path_copy = path.copy()
            #Add the parent to the path
            path_copy.append(parent)
            #Queue of the copy
            queue.enqueue(path_copy)
    #Return the earliest ancestor
    return earliest_ancestor


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (11, 10), (12, 10)]

# print(earliest_ancestor(test_ancestors, 3))