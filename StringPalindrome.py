get_string = input("Enter a string: ")
new_string = get_string.replace(" ", "").lower()
reverse_string = new_string[::-1]

# ============
# # Check if the string is a palindrome
# if new_string == reverse_string:
#     print(f"{get_string} is a palindrome.")
# else:
#     print(f"{get_string} is not a palindrome.")

# # ============
# # Check if the single word string is a palindrome
# if get_string.lower() == get_string[::-1].lower():
#     print(f"{get_string} is a palindrome.")
# else:
#     print(f"{get_string} is not a palindrome.")


# # ============
# if get_string.lower().replace(" ", "") == get_string[::-1].lower().replace(" ", ""):
#     print(f"{get_string} is a palindrome.")
# else:
#     print(f"{get_string} is not a palindrome.")


# # ============
# def is_palindrome(s):
#     # Remove spaces and convert to lowercase
#     s = s.replace(" ", "").lower()
#     # Check if the string is equal to its reverse
#     return s == s[::-1]

# if is_palindrome(get_string):
#     print(f"{get_string} is a palindrome.")
# else:
#     print(f"{get_string} is not a palindrome.")
