import math
allowanceMoney = float(input("Enter the allowance amount: "))

milk = 0.45
rawCider = 3.85
flour = 0.90
butter = 0.77
nutella = 1.87

orderPrice = 2*milk + 3*rawCider + 1*flour + 1*butter + 1*nutella
print(f"Your order sums up to {orderPrice:.2f}")

"""Using math.isclose() method to compare the allowance and the order amounts
since using regular == comparison returns true due to rounding errors"""
if math.isclose(allowanceMoney,orderPrice, rel_tol=1e-2):
    message = "You are broke!"
elif allowanceMoney < orderPrice:
    message = f"Sorry you're missing {abs(allowanceMoney-orderPrice):.2f} euros"
elif allowanceMoney > orderPrice:
    message = f"You have spent {orderPrice:.2f}. You have left with {allowanceMoney-orderPrice:.2F}"

print(message)