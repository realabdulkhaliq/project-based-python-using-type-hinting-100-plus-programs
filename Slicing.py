mylist: list = ['abu bakar', 'umar', 'usman', 'ali']

print(mylist[0:2])  # ['abu bakar', 'umar']
print(mylist[0:3])  # ['abu bakar', 'umar', 'usman']
print(mylist[0:5])  # ['abu bakar', 'umar', 'usman', 'ali']
print(mylist[0:6])  # ['abu bakar', 'umar', 'usman', 'ali']


print(mylist[-1:])  # ['ali']
print(mylist[::-1])  # ['ali', 'usman', 'umar', 'abu bakar']
print(mylist[::-2])  # ['ali', 'umar']

print(mylist[::2])  # ['abu bakar', 'usman']
print(mylist[-2:-4])  # []
print(mylist[-2:-5])  # []
print(mylist[-4:-2])  # ['abu bakar', 'umar']
print(mylist[-4:-1])  # ['abu bakar', 'umar', 'usman']