marks = int(input("Enter marks of Student: "))

if marks >= 90:
    print(f"Grade 'A' (marks = {marks})")
elif marks >= 80 and marks < 90:
    print(f"Grade 'B' (marks = {marks})")
elif marks >= 70 and marks < 80:
    print(f"Grade 'C' (marks = {marks})")
else:
    print(f"Grade 'D' (marks = {marks})")