import collections.abc as c
import numpy as np

'''Linked List
Contains node w/1 element, and a head that points to the next node'''

class Node:
    def __init__(self, e):
        self.element = e
        self.__next = None      
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, value):
        if isinstance(value, Node):
            self.__next = value

class MyAbstractList(c.Iterator):
    def __init__(self, list_items):
        # iterate over every element and call self.append(item)
        self.size = 0
        self._idx = 0
        for item in list_items:
            self.append(item)
    @property
    def is_empty(self):
        return (self.size == 0)
    def append(self, item):
        # call add_at() method here
        self._add_at(self.size,item)       
    def remove(self, item):
        # you should use remove_at() method here
        idx = self._index_of(item)
        if idx >=0:
            self._remove_at(item)
            return True
        else:
            return False     
    def __getitem__(self, index):
        return self._get(index)
    def __setitem__(self, index, value):
        # call set_at(index, value) method here
        self._set_at(index,value)   
    def __delitem__(self, index):
        # call remove_at() method here
        self._remove_at(index)
    def __len__(self):
        return self.size
    def __iter__(self):
        self._idx = 0
        return self 
    def __next__(self):
        if self._idx < self.size:
            n_item = self._get(self._idx)
            self._idx += 1
            return n_item
        else:
            raise StopIteration
    # the following methods should be implemented in the child class
    def _get(self, index):
        pass
    def _set_at(self, index, item):
        pass
    def _add_at(self, index, item):
        pass
    def _remove_at(self, index):
        pass

class MyLinkedList(MyAbstractList):
    def __init__(self, items):
        self.head = None
        self.tail = None
        super().__init__(items)
    def _goto(self,index): # go to the node object at the index
        current = self.head
        for i in range(index+1):
            if i == index:
                return current
            current = current.next
    def _get(self, index):
        # do the following:
        # 1. traverse to the node at index
        # 2. return the element of that node
        current = self.head
        for i in range(index+1):
            if i == index:
                return current.element
            current = current.next  
    def _add_first(self, element):
        # do the following:
        # 1. create a new Node object using element
        # 2. set the current head reference as the next reference of the new node
        # 3. increase size by 1
        # 4. if this is the last element (no tail) -> set the current node as the tail
        n = Node(element)
        n.next = self.head
        self.head = n
        self.size += 1
        if self.size == 1:
            self.tail = n
    def _add_last(self, element):
        # do the following:
        # 1. create a new Node object using element
        # 2. if there is no element as tail -> set the new node as both
        #    the tail and the head
        # 3. otherwise, -> 
        #    - set the new node as the next reference of the tail
        #    - set the next reference of the current node as the tail's next reference
        # 4. increase size by 1
        n = Node(element)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            self.tail = n
            last_node = self._goto(self.size-1)
            last_node.next = n
        self.size += 1
    def _add_at(self, index, element):
        if index == 0:
            # if insert at first position, call add_first() method
            self._add_first(element)
        elif index >= self.size:
            # if insert at last position, call add_last() method
            self._add_last(element)
        else:
            # if insert in between, do the following:
            # 1. start from the head, traverse the linked list to get
            #    the reference at position index-1 using its next reference
            # 2. create a new Node
            # 3. set the next of the current node as the next of the new Node
            # 4. set the new node as the next of the current node
            # 5. increase the size by 1
            n = Node(element)
            prev_node = self._goto(index-1)
            after_node = self._goto(index)
            prev_node.next = n
            n.next = after_node
            self.size += 1
    def _set_at(self, index, element):
        if 0 <= index < self.size:
            current = self._goto(index)
            current.element = element    
    def _remove_first(self):
        if self.size == 0:
            # if list is empty, return None
            return None
        else:
            # otherwise, do the following:
            # 1. store the head at a temporary variable
            # 2. set the next reference of the current head to be the head
            # 3. reduce size by 1
            # 4. if the new head is now None, it means empty list
            #    -> set the tail to be None also
            # 5. return element of the removed node
            temp = self.head
            self.head = temp.next
            self.size -=1
            if self.head == None:
                self.tail = None
            return temp.element 
    def _remove_last(self):
        if self.size == 0:
            # if the list is empty, return None
            return None
        elif self.size == 1:
            # if there is only one element, just remove that one node 
            # using some other method
            return self._remove_first()
        else:
            # otherwise, do the following:
            # 1. traverse to the second last node
            # 2. store the tail of the list to a temporary variable
            # 3. set the current node as the tail
            # 4. set the next ref of the tail to be None
            # 5. reduce the size by 1
            # 6. return the element of the removed node in the temp var
            prev_node = self._goto(self.size-2)
            temp = self.tail
            self.tail = prev_node
            prev_node.next = None
            self.size -= 1
            return temp.element
    def _remove_at(self, index):
        if index < 0 or index >= self.size:
            return None
        elif index == 0:
            return self._remove_first()
        elif index == self.size - 1:
            return self._remove_last()
        else:
            # do the following:
            # 1. traverse to the node at index - 1
            # 2. get the node at index using next reference
            # 3. set the next node of the node at index - 1
            # 4. decrease the size by 1
            # 5. return the element that is removed
            prev_node = self._goto(index-1)
            curr_node = self._goto(index)
            next_node = self._goto(index+1)
            prev_node.next = next_node
            self.size -= 1
            return curr_node.element

'''Fixed Size Array
Array with fixed size and element type'''

class ArrayFixedSize(c.Iterable):
    def __init__(self, size, dtype=int):
        self.__data = np.empty(size)
        self.__data = self.__data.astype(dtype)    
    def __getitem__(self, index):
        return self.__data[index]
    def __setitem__(self, index, value):
        self.__data[index] = value      
    def __iter__(self):
        return iter(self.__data)
    def __len__(self):
        return len(self.__data) 
    def __str__(self):
        out = "["
        for item in self:
            out += f"{item:}, "
        if self.__data != []:
            return out[:-2] + "]"
        else:
            return "[]"