def merg_sort(array):
    if len(array)>1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        
        #recursion
        merg_sort(left_array)
        merg_sort(right_array)
        
        #merge
        i = 0 # the left most in the first array
        j = 0 # the left most in the second array
        k = 0 # merged array index
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i+=1
            else:
                array[k] = right_array[j]
                j+=1
            k+=1
        while i < len(left_array):
            array[k] = left_array[i]
            i +=1
            k +=1
        while j < len(right_array):
            array[k] = right_array[j]
            j +=1
            k+=1
                
array = [4, 5, 322, 53, 32, 3]
merg_sort(array)
print(array)