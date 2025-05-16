A = [[1,2,3], [4,5,6]]

T = [[0,0], [0,0], [0,0]]

# Transpose the matrix

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]


# Print the transposed matrix
for r in T:
    print(r)


# Transpose the matrix using list comprehension
L = [ [A[j][i] for j in range(len(A))] for i in range(len(A[0]))]