def fibo(n):
    if n <= 1:
        return n
    else:
        # print(n-1, n-2)
        # return fibo(n - 1)
        # return fibo(n - 2)
        return fibo(n - 1) + fibo(n - 2)
    

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibo(i), end=" ")

# print(fibo(5))



