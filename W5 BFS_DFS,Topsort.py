import sys

class Stack:
    def __init__(self):
        self.__items = []     
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        if len(self.__items) == 0:
            return None
        return self.__items.pop()
    def peek(self):
        if len(self.__items) == 0:
            return None
        return self.__items[-1]
    @property
    def is_empty(self):
        if len(self.__items) == 0:
            return True
        return False
    @property
    def size(self):
        return len(self.__items)
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

class VertexSearch(Vertex):
    def __init__(self, id_=""):
        super().__init__(id_)
        self.colour = "white"
        self.d = sys.maxsize
        self.f = sys.maxsize
        self.parent = None

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


class SearchBFS(Search2D):
    def search_from(self, start):
        q = Queue()
        self.clear_vertices()
        start_v = self.graph.vertices[start]
        start_v.colour = "grey"
        start_v.d = 0
        start_v.parent = None       
        q.enqueue(start_v)       
        while not q.is_empty:
            u = q.dequeue()
            for neighbour in u.get_neighbours():
                neighbour_object = self.graph.vertices[neighbour]
                if neighbour_object.colour == "white":
                    neighbour_object.colour = "grey"
                    neighbour_object.d = u.d+1
                    neighbour_object.parent = u
                    q.enqueue(neighbour_object)
                u.colour = "black"        
    def get_shortest_path(self, start, dest):
        if (start not in self.graph.vertices) or (dest not in self.graph.vertices):
            return None
        self.search_from(start)
        result = []
        self.get_path(start, dest, result)
        return result[::-1]       
    def get_path(self, start, dest, result):
        if dest == start:
            result.append(dest)
            return result
        elif self.graph.vertices[dest].parent is None:
            result.append("No Path")
            return result
        else:
            result.append(dest)
            self.get_path(start, self.graph.vertices[dest].parent.id_, result)


class SearchDFS(Search2D):
    def __init__(self, g):
        self.graph = g
        self.time = 0     
    def search(self):
        self.clear_vertices()
        self.time = 0
        for vertex in self.graph:
            if vertex.colour == "white":
                self.dfs_visit(vertex) 
    def dfs_visit(self, vert):
        self.time += 1
        vert.d = self.time
        vert.colour = "grey"
        for n in vert.get_neighbours():
            n_obj = self.graph.vertices[n]
            if n_obj.colour == "white":
                n_obj.parent = vert
                self.dfs_visit(n_obj)
        vert.colour = "black"
        self.time += 1
        vert.f = self.time


def topological_sort(g):
    result = []
    g.search()
    obj_list = [i for i in g.graph.vertices.values()]
    return sorted(obj_list, key = lambda x: x.f, reverse = True)