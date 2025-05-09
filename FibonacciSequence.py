a = 0
b = 1

n = int(input("Enter the term till you want to print fibonacci sequence: "))

for i in range(0, n):
    print(a, end=" ")   # 0                    a = 1
    c = a + b           # 0 + 1 = 1            1 + 1 c = 2  
    a , b = b , c       # a= 1 , b = 1         a = 1 , b = 2


