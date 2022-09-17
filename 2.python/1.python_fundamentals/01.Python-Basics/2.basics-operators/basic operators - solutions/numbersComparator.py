while True:
    a = float(input("Enter number A: "))
    b = float(input("Enter number B: "))
    if a<b:
        print(f"A is smaller than B - {a}")
    elif b<a:
        print(f"B is smaller than A - {b}")
    else:
        print("A and B are equal")
'''wrapped in While loop to make testing easier'''
