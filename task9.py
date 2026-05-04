class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def display(self):
        return self.queue


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

if __name__ == "__main__":
    q = Queue()

    # Insert elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    print("Queue elements:", q.display())

    key = int(input("Enter element to search: "))

    result = linear_search(q.display(), key)

    if result != -1:
        print("Element found at position", result + 1)
    else:
        print("Element not found")