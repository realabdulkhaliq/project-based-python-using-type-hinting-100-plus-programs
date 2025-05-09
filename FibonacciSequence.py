a = 0
b = 1

n = int(input("Enter the term till you want to print fibonacci sequence: "))

for i in range(0, n):
    print(a, end=" ")   # 0                    a = 1
    c = a + b           # 0 + 1 = 1            1 + 1 c = 2  
    a , b = b , c       # a= 1 , b = 1         a = 1 , b = 2


if n == 0:
    print(a)
else:
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        a , b = b , c
        print(c, end=" ")