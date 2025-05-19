input_string = input("Enter a string: ")

new_string = input_string.split() # Split the string into list of words

# for i in range(len(new_string)):
#     new_string[i] = new_string[i].lower()

new_string.sort() # Sort the list of words

for i in new_string: # iterate through each word in the list
    print(i, end=" ")