import math

def indexed_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return i

    return -1

arr = [5, 10, 15, 20, 25, 30]
key = int(input("Enter element: "))

if indexed_search(arr, key) != -1:
    print("Element found")
else:
    print("Element not found")