import sys

class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()
    def enqueue(self,item):
        self.right_stack.push(item)    
    def dequeue(self):
        if self.left_stack.size == 0:
            while self.right_stack.size > 0:
                item = self.right_stack.pop()
                self.left_stack.push(item)
        return self.left_stack.pop()
    @property
    def is_empty(self):
        if self.left_stack.size + self.right_stack.size == 0:
            return True
        else:
            return False
    @property
    def size(self):
        return self.left_stack.size + self.right_stack.size    
    def peek(self):
        if self.left_stack.size == 0:
            while self.right_stack.size > 0:
                item = self.right_stack.pop()
                self.left_stack.push(item)
        return self.left_stack.peek()

class Vertex:
    def __init__(self, id_=""):
        self.id_ = id_  #id is a built-in function in python, hence we use id_
        self.neighbours = {}
    
    def add_neighbour(self, nbr_vertex, weight=0):
        self.neighbours[nbr_vertex] = weight
    
    def get_neighbours(self):
        return [key for key in self.neighbours.keys()]
    
    def get_weight(self, neighbour):
        if neighbour not in self.neighbours:
            return None
        return self.neighbours[neighbour]
    
    def __eq__(self, other):
        return self.id_ == other.id_
    
    def __lt__(self, other):
        return self.id_ < other.id_
    
    def __hash__(self):
        return hash(self.id_)
    
    def __str__(self):
        neighbour_list = self.get_neighbours()
        id_list = [i.id_ for i in neighbour_list]
        id_str = ", ".join(id_list)
        return "Vertex {} is connected to: {}".format(self.id_,id_str)

class Graph:
    def __init__(self):
        self.vertices = {}
        
    def _create_vertex(self, id_):
        return Vertex(id_)
    
    def add_vertex(self, id_):
        vertex = self._create_vertex(id_)
        self.vertices[id_] = vertex
    
    def get_vertex(self, id_):
        if id_ not in self.vertices:
            return None
        return self.vertices[id_]
    
    def add_edge(self, start_v, end_v, weight=0):
        self.vertices[start_v].add_neighbour(end_v, weight)
    
    def get_neighbours(self, id_):
        if id_ not in self.vertices:
            return None
        return self.vertices[id_].get_neighbours()
    
    def __contains__(self, val):
        if val in self.vertices.keys():
            return True
        return False
    
    def __iter__(self):
        for k,v in self.vertices.items():
            yield v 
        
    # write a code to create a computed property called num_vertices
    @property
    def num_vertices(self):
        return len([i for i in self.vertices.keys()])

class GraphSearch(Graph):
    def __init__(self):
        super().__init__()
    def _create_vertex(self, id_):
        return VertexSearch(id_)

class Search2D:
    def __init__(self, g):
        self.graph = g
    
    def clear_vertices(self):
        for VertexSearch in self.graph.vertices.values():
            VertexSearch.colour = "white"
            VertexSearch.d = sys.maxsize
            VertexSearch.f = sys.maxsize
            VertexSearch.parent = None
    
    def __iter__(self):
        return iter([v for v in self.graph])
    
    def __len__(self):
        return len([v for v in self.graph.vertices])