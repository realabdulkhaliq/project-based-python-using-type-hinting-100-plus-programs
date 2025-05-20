punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# punctuation1 = [!()-[]{};:'"\,<>./?@#$%^&*_~] error

get_string = input("Enter a string: ")
new_string = ""
for char in get_string:
    if char not in punctuation:
        new_string += char
print("String without punctuation:", new_string)


