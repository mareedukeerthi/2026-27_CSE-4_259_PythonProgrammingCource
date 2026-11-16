S1 = input("Enter String 1: ")
S2 = input("Enter String 2: ")

if sorted(S1) == sorted(S2):
    print("Anagrams")
else:
    print("Not anagrams")