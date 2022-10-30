'''Stack: First In, Last Out type of array'''

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


'''Queue: First In, First Out type of array
Implements 2 Stacks, with a has-a relationship'''

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


'''EvaluatePostfix'''

class EvaluatePostfix:
    operands = "0123456789" # class attribute, what we usually have is instance attributes
    operators = "+-*/"
    def __init__(self):
        self.expression = [] # instance attribute
        self.stack = Stack()
    def input(self, item):
        self.expression.append(item)
    def evaluate(self):
        while len(self.expression) > 0:
            i = self.expression[0]
            del self.expression[0]
            if i in EvaluatePostfix.operands:
                self.stack.push(int(i))
            else:
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                if i == "+":
                    self.stack.push(n1+n2)
                elif i == "-":
                    self.stack.push(n2-n1)
                elif i == "*":
                    self.stack.push(n1*n2)
                elif i == "/":
                    self.stack.push(n2/n1)
        return self.stack.pop()


'''RadixSort'''

class RadixSort:
    def __init__(self, MyList):
        self.items = MyList
        self.main_bin = Queue()
        self.digit_bins = {"0":Queue(), "1":Queue(), "2":Queue(), "3":Queue(), "4":Queue(),\
                           "5":Queue(), "6":Queue(), "7":Queue(), "8":Queue(), "9":Queue(),}
    def max_digit(self):
        return len(str(max(self.items)))
    def convert_to_str(self, items):
        max_digit = self.max_digit()
        str_list = [str(i) for i in items]
        # Changing all the items in the list into strings of the same length
        # e.g. [23, 1038, 8, 423, 10] -> ['0023', '1038', '0008', '0423', '0010']
        for i in range(len(str_list)):
            if len(str_list[i]) < max_digit:
                add = max_digit-len(str_list[i])
                str_list[i] = add * "0" + str_list[i]       
        return str_list
    def sort(self):
        max_digit = self.max_digit()
        str_list = self.convert_to_str(self.items)   
        # Adding all items in the string list to the main queue
        for i in str_list:
            self.main_bin.enqueue(i) 
        # Performing the sort
        for index in range(max_digit-1,-1,-1):
            while not self.main_bin.is_empty:
                string = self.main_bin.dequeue()
                self.digit_bins[string[index]].enqueue(string)
            for queue in self.digit_bins.values():
                while not queue.is_empty:
                    string2 = queue.dequeue()
                    self.main_bin.enqueue(string2)
        sorted_list = self.main_bin._Queue__items
        # Stripping the "0"s we added from the left and converting to string
        result_str = [string.lstrip("0") for string in sorted_list]
        result_int = [int(i) for i in result_str]
        # Tada!
        return result_int
                