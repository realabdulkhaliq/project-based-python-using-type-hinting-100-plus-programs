string = "Microsoft Certified: Generative AI Engineer, GitHub Certified: Cloud Security Engineer"
char = "e"
count = 0

for i in string:
    if i == char:
        count += 1

print(f"The character '{char}' occurs {count} times in the string '{string}'.")

