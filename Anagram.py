str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) == len(str2) and sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")