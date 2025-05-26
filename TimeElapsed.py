import time

starting_time = time.time()

print("Hello, World!")
# This code prints "Hello, World!" and measures the time taken to execute this print statement.

ending_time = time.time()
print(f"Time taken to execute the print statement: {ending_time - starting_time:.4f} seconds")


def time_elapsed(func):
    """
    Decorator to measure the time elapsed for a function to execute.
    
    Args:
        func (callable): The function to be decorated.
        
    Returns:
        callable: The wrapped function that measures execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time elapsed for {func.__name__}: {elapsed_time:.4f} seconds")
        return result
    
    return wrapper