class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def display(self):
        return self.stack
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
if __name__ == "__main__":
    stack = Stack()

    stack.push(64)
    stack.push(25)
    stack.push(12)
    stack.push(22)
    stack.push(11)

    print("Original Stack:", stack.display())

    arr = stack.display().copy()
    sorted_arr = selection_sort(arr)

    print("Sorted Stack:", sorted_arr)