s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# spaces theesi, small letters lo ki marchadam
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")