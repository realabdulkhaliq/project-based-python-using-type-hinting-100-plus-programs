def DeciToBinary(n):
    """Convert a decimal number to binary using recursion."""
    if n > 1:
        DeciToBinary(n // 2)
    print(n % 2, end='')

