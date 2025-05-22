get_string = input("Enter a string: ")
new_string = get_string.replace(" ", "").lower()
reverse_string = new_string[::-1]

# ============
# # Check if the string is a palindrome
# if new_string == reverse_string:
#     print(f"{get_string} is a palindrome.")
# else:
#     print(f"{get_string} is not a palindrome.")

