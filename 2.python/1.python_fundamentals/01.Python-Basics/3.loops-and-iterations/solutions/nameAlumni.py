all_students = [
    ["David", "Justine", "Valentin", "Axel", "Redouane"],
    ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"],
]
i=0;m=0
for a in range(2):
    for b in range(5):
        print(f"{all_students[i][m]} is an alumni")
        m+=1
    i+=1;m=0

