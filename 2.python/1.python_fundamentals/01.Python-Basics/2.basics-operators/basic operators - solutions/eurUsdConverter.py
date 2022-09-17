convType = input("Currency that you are entering - (E)uros or ($)ollars: ")
initialAmount = float(input("Enter the amount: "))
"""Today 16/09/2022 the EUR and USD are on par with each other
Using 1.15 as an example so the program actually does something"""
if convType.upper() == "E":
    resultAmount = initialAmount*1.15
    print(f"The sum you entered equals to {resultAmount:.2f} USD")
elif convType == "$":
    resultAmount = initialAmount/1.15
    print(f"The sum you entered equals to {resultAmount:.2f} EUR")
else:
    print("Please try again")