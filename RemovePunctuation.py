punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# punctuation1 = [!()-[]{};:'"\,<>./?@#$%^&*_~] error

get_string = input("Enter a string: ")
new_string = ""
for char in get_string:
    if char not in punctuation:
        new_string += char
print("String without punctuation:", new_string)


# Function to remove punctuation from a string

def remove_punctuation(input_string):
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', punctuation)
    # Use the translate method to remove punctuation
    return input_string.translate(translator)
# Example usage
input_string = "Hello, World! This is a test string with punctuation."
output_string = remove_punctuation(input_string)
print("Original string:", input_string)
print("String without punctuation:", output_string)