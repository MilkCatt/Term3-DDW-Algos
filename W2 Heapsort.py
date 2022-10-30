list1 = [16,14,10,8,7,8,3,2,4,1]

'''Heapsort
Views the array as a binary tree and builds a minimum heap
Once a minimum heap is built, the top node is taken and placed into a sorted array
'''

#Obtains the left child node index
def left_of(index): 
   return 2*index+1

#Obtains the right child node index
def right_of(index): 
   return (index+1)*2

#Obtains the index of the lowest value child node
def min_child(heap, index):
   if right_of(index)<len(heap):
      if heap[right_of(index)] < heap[left_of(index)]:
         return right_of(index)
   return left_of(index)

#Creates a minimum heap, assuming all nodes below are a minimum heap
def min_heapify(array, index, size):
   current_i = index
   swapped = True
   #While the we current node does still have a child node
   while (left_of(current_i)<len(array)) and swapped:
      swapped = False
      #Obtain the min_child
      min_child_i = min_child(array,current_i)
      #If the min child is less than its parent node
      if array[min_child_i]<array[current_i]:
         #swap
         array[min_child_i],array[current_i] = array[current_i],array[min_child_i]
         swapped = True
      current_i = min_child_i

#Creating a minimum heap from an array by calling min_heap from midway through the array (no child nodes)
def build_min_heap(array):
   n = len(array)
   starting_index = int(n//2)-1
   for i in range(starting_index,-1,-1):
      min_heapify(array,i,n)

#Heapsort algo with heapify already implemented
def heapsort(array):
   result = [] #A separate array to store items
   build_min_heap(array) #Building a min heap for the array
   heap_end_pos = len(array)-1 #reducing the heap size as the 
   while (heap_end_pos>=0):
      result.append(array[0])
      array[0],array[heap_end_pos] = array[heap_end_pos],array[0]
      array = array[0:heap_end_pos]
      heap_end_pos -= 1
      min_heapify(array,0,len(array))
   return result


print(heapsort(list1))