
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

count = 0
def fib_recursive(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

n = int(input("Enter n: "))

print("Iterative:", fib_iterative(n))
count = 0
print("Recursive:", fib_recursive(n))
print("Recursive calls:", count)