my_string = "Microsoft Certified: Generative AI Engineer, GitHub Certified: Cloud Security Engineer"
vowels = "aeiou"
count = 0
for char in my_string.lower():
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)
# This code counts the number of vowels in a given string.

# # ========================
# # Using a dictionary to count occurrences of each vowel
# my_string = my_string.casefold()
# count = {}.fromkeys(vowels, 0)
# for char in my_string:
#     if char in count:
#         count[char] += 1

# print("Count of vowels in the string:", count)
# # This code counts the occurrences of each vowel in a given string.

# ========================
# Using dictionary comprehension
count = {key: sum ( [ 1 for char in my_string if char == key ] ) for key in vowels }
print("Count of vowels in the string:", count)
# This code counts the occurrences of each vowel in a given string using dictionary comprehension.