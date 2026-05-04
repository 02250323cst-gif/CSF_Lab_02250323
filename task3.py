def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for k in range(i+1, n):
            if arr[k] < arr[min_index]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted List:", selection_sort(arr))