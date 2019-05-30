# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph
from getDistance import countries_links



def place(i):
    switcher = {
        "Kuala Lumpur":0 ,
        "Beijing":1 ,
        "Singapore":2 ,
        "Brunei":3 ,
        "Jakarta":4 ,
        "Taipei":5 ,
        "Melbourne":6 ,
        "Tokyo":7 ,
        'Hanoi':8 ,
    }
    return switcher.get(i, "Invalid place")

# Class to represent a graph
class Graph:



    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

        # Function to print shortest path

    # from source to j
    # using parent array
    def printPath(self, parent, j):
        showPath = "->"
        def place(i):
            switcher = {
                0: "Kuala Lumpur",
                1: "Beijing",
                2: "Singapore",
                3: "Brunei",
                4: "Jakarta",
                5: "Taipei",
                6: "Melbourne",
                7: "Tokyo",
                8: 'Hanoi',
            }
            return switcher.get(i, "Invalid place")
        # Base Case : If j is source
        if parent[j] == -1:

            print(place(0), end = '')
            return
        self.printPath(parent, parent[j])
        print (showPath + place(j), end = '')

        # A utility function to print

    # the constructed distance
    # array
    def printSolution(self, dist, parent,destination):
        print("Shortest Path")
        print("\nRoute \t\t\t\t\t\t\t\t\t\t\t\t\tDistance from Source\t\t\t\tShortest Path")

        def place(i):
            switcher = {
                0: "Kuala Lumpur",
                1: "Beijing",
                2: "Singapore",
                3: "Brunei",
                4: "Jakarta",
                5: "Taipei",
                6: "Melbourne",
                7: "Tokyo",
                8: 'Hanoi',
            }
            return switcher.get(i, "Invalid place")
        print("%s --> %s \t\t\t\t\t\t\t\t\t\t%d \t\t\t\t\t" % (place(0), place(destination), dist[destination]), end = ''),self.printPath(parent, destination)

    '''Function that implements Dijkstra's single source shortest path 
    algorithm for a graph represented using adjacency matrix 
    representation'''

    def dijkstra(self, graph, src, des):

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        # Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)

            # Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist, queue)

            # remove min element
            queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is 
                an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of 
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

                        # print the constructed distance array
        self.printSolution(dist, parent,des)

allPathDistance = countries_links

# print(allPathDistance)
# print(allPathDistance[0][1])
# print(place(allPathDistance[0][0]))
# print(place(allPathDistance[0][1]))
# print(allPathDistance)
g2 = Graph()
list1 = []
list2 = []
for i in range(0,9):
    list1.append(0)
    list2.append(list1)
w, h = 9, 9;
Matrix = [[0 for x in range(w)] for y in range(h)]
# print(Matrix)

for row in range(16):
    location1 = place(allPathDistance[row][0])
    # print(location1)
    location2 = place(allPathDistance[row][1])
    # print(location2)
    distance =allPathDistance[row][2]
    Matrix[location1][location2] = distance
# print(Matrix)

graph = Matrix


# graph =   [[0, 4334.15, 308.76, 1456.62, 1182.06, 3226.14, 0, 0, 0],
#            [4334.15, 0, 0, 0, 0, 1718.13, 0, 2093.92, 0],
#            [308.76, 0, 0, 1262.56, 0, 3240.80, 6054.34, 0, 0],
#            [1456.62, 0, 1262.56, 0, 1476.12, 0, 5634.93, 0, 2062.60],
#            [1182.06, 0, 0, 1476.12, 0, 0, 0, 0, 3014.73],
#            [3226.14, 1718.13, 3240.80, 0, 0, 0, 7374.29, 2095.50, 0],
#            [0, 0, 6054.34, 5634.53, 0, 7374.29, 0, 0, 0],
#            [0, 2093.92, 0, 0, 0, 2095.50, 0, 0, 0],
#            [0, 0, 0, 2062.60, 3014.73, 0, 0, 0, 0]
#            ]
# print(Matrix)