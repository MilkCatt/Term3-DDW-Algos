list1 = [16,14,10,8,7,8,3,2,4,1]

'''Insertion Sort
Sorts an array in place by starting from the 2nd element.
moves element to the left until it is larger than the number on its left.
Outer loop: runs n-1 times
Inner loop: runs n-1 times
Optimisation: Instead of swapping each time, store the identified variable in a temp var.
              Take this temp var and move it until the item on the left is smaller.
              This reduces the number of assignments.
Time Complexity: O(n^2)'''

def insertion_sort(ls):
   n = len(ls)
   for outer_index in range(1,n):
      inner_index = outer_index #Gets the item in question
      temp_var = ls[inner_index] #Optimisation: stores it into a variable
      while (inner_index>0) and (temp_var<ls[inner_index-1]): #Condition: item on left is smaller and we have not reached list start
         ls[inner_index] = ls[inner_index-1] #Shifts the compared item to the right
         inner_index = inner_index-1
      ls[inner_index] = temp_var
   return(ls)


insertion_sort(list1)
print(list1)