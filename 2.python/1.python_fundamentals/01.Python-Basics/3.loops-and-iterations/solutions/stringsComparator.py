a = input("Enter string a: ")
b = input("Enter string b: ")
if len(a)>len(b):
    print("String a is longer:")
    print(a)
elif len(a)<len(b):
    print("String b is longer:")
    print(b)
else:
    print("a and b are equal")
    