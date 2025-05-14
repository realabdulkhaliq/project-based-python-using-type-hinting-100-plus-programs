A = [[2,3,4],
     [5,6,7],
     [8,9,10]]

B = [[1,2,3],
     [4,5,6],
     [7,8,9]]
# Initialize the result matrix C with zeros
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]

# Add the two matrices A and B

for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]
