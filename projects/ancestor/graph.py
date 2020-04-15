"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #Create a stack
        stack = Stack()
        # Create a set of traversed vertices
        visited = set()
        #Put starting vertext in created stack
        stack.push(starting_vertex)

        #While the stack has something in it
        while stack.size() > 0:
            #Set current node as the starting vertex
            current_node = stack.pop()

            #If the current node has not been visited
            if current_node not in visited:
                print(current_node)
                #Add it to visited set
                visited.add(current_node)
                #Get what its connected too
                edges = self.get_neighbors(current_node)
                
                #Push everything its connected to into visited and repeat
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
         #Change the input to take the visited set
        #If the starting vertex is not in the visited set
        if starting_vertex not in visited:
            #Add it to visited
            visited.add(starting_vertex)
            print(starting_vertex)
            #For each neighbor of the vertext
            for neighbor in self.get_neighbors(starting_vertex):
                #Recursion passing in that neighbor and the visited set
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Create a Queue and put in the starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        
        # Create a set of traversed vertices
        visited = set()

        #While there are items in the queue
        while queue.size() > 0:
            
            #set the path as the current queue item, and remove from queue
            path = queue.dequeue()
            #Set the current node from  the end of the path
            current_node = path[-1]
            #If the current node is not in visited
            if current_node not in visited:
                #Visit it 
                visited.add(current_node)
                #If the the current node is the destination return the path
                if current_node == destination_vertex:
                    return path
                #For each neighbor of the current node
                for neighbor in self.get_neighbors(current_node):
                    #Queue the path and the neighbor
                    queue.enqueue([*path, neighbor])

# queue: [1,2,3,5], [1,2, 4]
# path: [1, 2, 3]
# current node: 3
# visited: 1, 2, 3


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #Normal set up but with a stack
        stack = Stack()
        stack.push([starting_vertex])

        visited = set()

        #While the stack has something in it
        while stack.size() > 0:
            #Set path to the stacks pop
            path = stack.pop()
            #Set the current node to the last item in the path
            current_node = path[-1]
            #If the current node hasnt been visited, visit it
            if current_node not in visited:
                visited.add(current_node)
                #If the current node is the destination return the path
                if current_node == destination_vertex:
                    return path
                #For each neightbor the current node has
                for neighbor in self.get_neighbors(current_node):
                    #add to the stack an array with the current path and the neighbor 
                    stack.push([*path, neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #Change the input to take the visited set
        #If the starting vertex has not been visited, visit it
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            #If the vertex is = to the destination vertex
            if starting_vertex == destination_vertex:
                return [starting_vertex]
        
            #For each neighbor of the vertex
            for neighbor in self.get_neighbors(starting_vertex):
                #Set the path to recurse with the neighbor as the starting vertex)
                path = self.dfs_recursive(neighbor, destination_vertex, visited)

                #If the path is is not none, and the destination is in the path
                if path is not None and destination_vertex in path:
                    #return the starting vertex and the path in an array
                    return [starting_vertex, *path]


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 5))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    #print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
