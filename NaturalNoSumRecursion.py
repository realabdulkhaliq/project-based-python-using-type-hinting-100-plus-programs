def NaturalNoSum(n):
    if n <= 1:
        return n
    else:
        return n + NaturalNoSum(n-1)

