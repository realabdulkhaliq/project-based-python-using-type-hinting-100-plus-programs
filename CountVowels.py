my_string = "Microsoft Certified: Generative AI Engineer, GitHub Certified: Cloud Security Engineer"
vowels = "aeiou"
count = 0
for char in my_string.lower():
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)
# This code counts the number of vowels in a given string.

