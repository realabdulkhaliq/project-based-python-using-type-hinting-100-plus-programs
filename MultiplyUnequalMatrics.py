A = [[2,3,4],
     [5,6,7],
     [8,9,10]]

B = [[1,2,3,1],
     [4,2,2,6],
     [1,1,4,2]]
# Initialize the result matrix C with zeros
R = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

# Matrix Multiplication
# Iterate through rows of A
for i in range(len(A)):
    # Iterate through columns of B
    for j in range(len(B[0])):
        # Iterate through rows of B
        for k in range(len(B)):
            R[i][j] += A[i][k] * B[k][j]


# Print the result
print("Matrix R:")
print(R)

print("Resultant matrix:")
for r in R:
    print(r)

# The above code multiplies two matrices A and B of unequal rows and columns and stores the result in matrix R.