# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         # print(n-1, n-2)
#         # return fibo(n - 1)
#         # return fibo(n - 2)
#         return fibo(n - 1) + fibo(n - 2)
    

# n = int(input("Enter the number of terms: "))
# print("Fibonacci sequence:")
# for i in range(n):
#     print(fibo(i), end=" ")

# # print(fibo(5))

# # Recursive Method (Inefficient for large n)
# # Iterative Method (Most Efficient)
# def fibo(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# n = int(input("Enter the number of terms: "))
# print("Fibonacci sequence:")
# fibo(n)

# Memoized Recursion (Improved Recursive Method)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibo(i), end=" ")



