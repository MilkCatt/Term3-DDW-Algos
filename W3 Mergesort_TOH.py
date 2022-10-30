input_array =[5, 2, 4, 7, 1, 3, 2, 6, 234, -34, 2,-44]

'''Mergesort
Uses recursion to continually split an array, compare, and merge arrays'''

#Non recursive, takes 2 SORTED arrays (1 array split into 2) and has pointers going through both.

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

   
mergesort(input_array)
print(input_array)