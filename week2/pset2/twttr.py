s = input("Input: ")
vowels = "aeiouAEIOU"
for c in s:
    if c not in vowels:
        print(c, end="")
print()
