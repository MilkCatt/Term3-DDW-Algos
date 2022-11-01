input_array =[5, 2, 4, 7, 1, 3, 2, 6, 234, -34, 2,-44]

'''Mergesort
Uses recursion to continually split an array, compare, and merge arrays
Computation time: O(nlogn)'''

# Non recursive, takes 2 SORTED arrays (1 array split into 2) and has pointers going through both
# Has a pointer going through each array, and stops 
def merge(array, l, m, r):
   # Setting Array Parameters to be used (splitting the left and right arrays)
   left_array = array[l:m]
   right_array = array[m:r+1]
   left_len = len(left_array)
   right_len = len(right_array)
   left_pointer = 0
   right_pointer = 0
   dest = l # Destination of the number to be added
   # While the pointers have not reached the end of their respective arrays
   while (left_pointer < left_len) and (right_pointer < right_len):
      # Compare values at pointers, then setting dest value
      if left_array[left_pointer] <= right_array[right_pointer]:
         array[dest] = left_array[left_pointer]
         left_pointer += 1
      else:
         array[dest] = right_array[right_pointer]
         right_pointer += 1
      dest += 1
   # Catching cases where one of the pointers have reached the end of their array
   while (left_pointer < left_len):
      array[dest] = left_array[left_pointer]
      left_pointer += 1
      dest += 1
   while (right_pointer < right_len):
      array[dest] = right_array[right_pointer]
      right_pointer += 1
      dest += 1

# Recursive function which continually splits and merges the function
def mergesort_recursive(array, l, r):
   if r-l > 0:
      m = (l+r)//2 
      mergesort_recursive(array, l, m)
      mergesort_recursive(array, m+1, r)
      merge(array, l, m+1, r)

# Helper function which gets the left and right index of the array
def mergesort(array):
   l = 0
   r = len(array)-1
   mergesort_recursive(array, l, r)

   
mergesort(input_array)
print(input_array)

'''TowerOfHanoi
Algo for moving disks from a source tower to a destination tower using an auxilliary tower
Computation Time: O(2^n)'''

def TowerOfHanoi(n , source, destination, auxiliary):
   # Base Case: if there is only 1 item in the tower, just move it to the destination
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    # Recursive Case: To form a tower of n disks, you must first for a tower of n-1 disks
    # at the auxilliary tower
    TowerOfHanoi(n-1, source, auxiliary, destination)
    # Move the final disk from source to destination
    print ("Move disk",n,"from source",source,"to destination",destination)
    # Move the auxilliary disks to the destination
    TowerOfHanoi(n-1, auxiliary, destination, source)