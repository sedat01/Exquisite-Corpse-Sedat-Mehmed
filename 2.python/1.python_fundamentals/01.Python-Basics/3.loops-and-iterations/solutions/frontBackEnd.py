languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]

i=0;m=0
for a in range(2):
    for b in range(3):
        if i==0:
            print(f"{languages[i][m]} is backend language?")
        else:
            print(f"{languages[i][m]} is frontend language?")
        m+=1
    i+=1;m=0