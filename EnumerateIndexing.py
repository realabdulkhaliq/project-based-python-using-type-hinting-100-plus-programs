mylist : list = ['a', 'b', 'c', 'd']

for index, value in enumerate(mylist):
    print(f"Index: {index}, Value: {value}")


for index, value in enumerate(mylist, start=1):
    # start=1 will start the index from 1 instead of 0
    print(f"Index: {index}, Value: {value}")