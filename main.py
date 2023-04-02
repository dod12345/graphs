graph = {}
# add vertex to the graph
def add_vertex(vertex):
    if vertex not in graph:
        graph[vertex] = []
# add edge to the graph
def add_edge(vertex1, vertex2):
    if vertex1 in graph:
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = [vertex2]
# get all vertices
def get_vertices():
    return list(graph.keys())
def define_gender(graph):
    gender = []
    for vertex in graph:
        # u:= undefined 
        gender[vertex] = "u"
def define_gender_for_vertex(graph,v,x):
    gender[v] = x
def female(v):
    define_gender_for_vertex(graph,v,"f")
def male(v):
    define_gender_for_vertex(graph,v,"m")
def check_valid(graph,v):
    inverse = getInverse(graph)
    if(len(inverse[v]) == 2):
        if(gender[inverse[v][0]] == "m" and gender[inverse[v][1]] == "f"):
            return True
        if(gender[inverse[v][0]] == "f" and gender[inverse[v][1]] == "m"):
            return True
    return False        
        
# get all edges
def get_edges():
    edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            edges.append((vertex, neighbor))
    return edges
def getInverse(graph):
    inverse = {}
    for vertex in graph:
        inverse[vertex] = []
        for node in graph:
            if(vertex in graph[node]):
                inverse[vertex].append(node)
    return inverse
# get all neighbors of a vertex
def get_neighbors(vertex):
    return graph[vertex]
def bfs(graph, start, end):
    queue = [start]
    visited = set([start])

    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False
    
    
def check_if_same_family(graph,v1,v2):# this function checks if two people in the builded graph are related
    inverse = getInverse(graph)
    for v in graph:
        if(bfs(graph, v1, v) == bfs(graph,v2,v)):
            return True
    return False        
# Example usage
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'D')
add_edge('C', 'D')
print(get_vertices())
print(get_edges())
print(get_neighbors('A'))
