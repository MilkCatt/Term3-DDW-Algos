list1 = [1000,1,4,7,3,10,100]

'''Bubble Sort
Sorts an array in place by comparing the pairs from left to right.
The algorithm will swap the 2 numbers if the number on the left is larger.
Outer loop: runs n-1 times (unoptimised)
Inner loop: runs n-1 times (unoptimised)
Optimisation 1: Outer loop stops when items are no longer swapped -> array si already sorted
Optimisation 2a: reduce inner index by 1 for each iteration (last 2 items will be sorted after each outer iteration)
Optimisation 2b: set the inner index to the index of the last item swapped (follows logic of 2a)
Computation Time : O(n^2)'''

def bubble_sort(ls):
   n = len(ls)
   swapped = True
   while swapped == True: # Optimisation 1 (Outer Loop)
      swapped = False
      new_n = 0 
      for inner_index in range(1,n): # Inner Loop
         first_number = ls[inner_index-1]
         second_number = ls[inner_index]
         if first_number > second_number: # Comparison, followed by swap
            ls[inner_index-1] = second_number
            ls[inner_index] = first_number
            swapped = True
            new_n = inner_index
      n = new_n # Optimisation 2
   return(ls)


bubble_sort(list1)
print(list1)
