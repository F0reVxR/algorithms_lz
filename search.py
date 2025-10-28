Array = [5,6,4,2]
m = 0
# loop to Traverse through all the elements in the given array
for i in range(len(Array)):
      
    # setting min_indx equal to the first unsorted element
    
    min_indx = i
    # Loop to iterate over un-sorted sub-array
    for j in range(i+1, len(Array)):
    
    #Finding the minimum element in the unsorted sub-array
        if Array[min_indx] < Array[j]:
            min_indx = j
            print(Array)
    # swapping the minimum element with the element at min_index to place it at its correct position    
    
    m = Array[i]
    Array[i] = Array[min_indx]
    Array[min_indx] = m
# Printing the modified array after the selection sort algorithm is applied

print(Array)