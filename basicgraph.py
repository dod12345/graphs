
# Online Python - IDE, Editor, Compiler, Interpreter

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		
		
def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        if parent[i] != i:
            return self.find_parent(parent, parent[i])
		
