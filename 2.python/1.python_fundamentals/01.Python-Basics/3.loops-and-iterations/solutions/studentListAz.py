'''This one combines the solutions for the first and second assignments'''
students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]

students.sort()
print(students)
i=0
for item in students:
    if students[i].startswith("M"):
        print(students[i])
    i+=1

