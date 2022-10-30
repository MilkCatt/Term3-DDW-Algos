### These algorithms sort arrays in place ###

list1 = [1000,1,4,7,3,10,100]
def bubble_sort(ls):
   n = len(ls)
   swapped = True
   while swapped == True:
      swapped = False
      new_n = 0
      for inner_index in range(1,n):
         first_number = ls[inner_index-1]
         second_number = ls[inner_index]
         if first_number > second_number:
            ls[inner_index-1] = second_number
            ls[inner_index] = first_number
            swapped = True
            new_n = inner_index
            print(ls)
      n = new_n
   return(ls)
# print(bubble_sort(list1))

list1 = [16,14,10,8,7,8,3,2,4,1]
def insertion_sort(ls):
   n = len(ls)
   for outer_index in range(1,n):
      inner_index = outer_index
      temp_var = ls[inner_index]
      while (inner_index>0) and (temp_var<ls[inner_index-1]):
         ls[inner_index] = ls[inner_index-1]
         inner_index = inner_index-1
      ls[inner_index] = temp_var
   return(ls)
print(insertion_sort(list1))

'''Heapsort, the most efficient method of sorting'''
def left_of(index):
   return 2*index+1

def right_of(index):
   return (index+1)*2

def min_child(heap, index):
   if right_of(index)<len(heap):
      if heap[right_of(index)] < heap[left_of(index)]:
         return right_of(index)
   return left_of(index)

def min_heapify(array, index, size):
   current_i = index
   swapped = True
   while (left_of(current_i)<len(array)) and swapped:
      swapped = False
      min_child_i = min_child(array,current_i)
      if array[min_child_i]<array[current_i]:
         array[min_child_i],array[current_i] = array[current_i],array[min_child_i]
         swapped = True
      current_i = min_child_i

def build_min_heap(array):
   n = len(array)
   starting_index = int(n//2)-1
   for i in range(starting_index,-1,-1):
      min_heapify(array,i,n)

def heapsort(array):
   result = []
   build_min_heap(array)
   heap_end_pos = len(array)-1
   while (heap_end_pos>=0):
      result.append(array[0])
      array[0],array[heap_end_pos] = array[heap_end_pos],array[0]
      array = array[0:heap_end_pos]
      heap_end_pos -= 1
      min_heapify(array,0,len(array))
   return result

print(heapsort(list1))

def merge(array, p, q, r):
   left_array = array[p:q]
   right_array = array[q:r+1]
   left_len = len(left_array)
   right_len = len(right_array)
   left_pointer = 0
   right_pointer = 0
   dest = p
   while (left_pointer < left_len) and (right_pointer < right_len):
      if left_array[left_pointer] <= right_array[right_pointer]:
         array[dest] = left_array[left_pointer]
         left_pointer += 1
      else:
         array[dest] = right_array[right_pointer]
         right_pointer += 1
      dest += 1
   while (left_pointer < left_len):
      array[dest] = left_array[left_pointer]
      left_pointer += 1
      dest += 1
   while (right_pointer < right_len):
      array[dest] = right_array[right_pointer]
      right_pointer += 1
      dest += 1
            
def mergesort_recursive(array, p, r):
   if r-p > 0:
      q = (p+r)//2 
      mergesort_recursive(array, p, q)
      mergesort_recursive(array, q+1, r)
      merge(array, p, q+1, r)

def mergesort(array):
   p = 0
   r = len(array)-1
   mergesort_recursive(array, p, r)
    
input_array =[5, 2, 4, 7, 1, 3, 2, 6, 234, -34, 2,-44]
mergesort(input_array)
print(input_array)