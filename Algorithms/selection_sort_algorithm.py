def selection_sorting(arr):
    for i in range(0, len(arr)-1):
        curr_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr_min]:
                curr_min = j
        arr[i], arr[curr_min] = arr[curr_min], arr[i]


arr = [1 ,23 , 4, 7, 8, 10, 23]
selection_sorting(arr)
print(arr)