A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 8, 11}
C = {4, 5}

# Union
print("Union of A and B:", A | B)
# Intersection
print("Intersection of A and B:", A & B)
# Difference
print("Difference of A and B:", A - B)
# Symmetric Difference
print("Symmetric Difference of A and B:", A ^ B)
# Subset
print("Is A a subset of B?", A <= B)
# Superset
print("Is A a superset of B?", A >= B)
# Disjoint Sets
print("Are A and B disjoint sets?", A.isdisjoint(B))
# Adding an element to a set
A.add(10)
print("Set A after adding 10:", A)
# Removing an element from a set
A.remove(1)
print("Set A after removing 1:", A)
# Clearing a set
C.clear()
print("Set C after clearing:", C)
# Copying a set
D = A.copy()
print("Copy of set A:", D)
# Length of a set
print("Length of set A:", len(A))
# Iterating through a set
for element in A:
    print("Element in set A:", element)