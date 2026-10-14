#Initialize variables for the fin.calculation
principle = 0
rate = 0
time = 0

#Input the principle amount(check so that it is not negative. If it is, ask for an input again all the way until it is bigger than or equal to 0)
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

#The same logic as principle amount. Asking and validating the interest rate
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break
#Validation of loop for time of years
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

#Calculating the compound interest using the mathematical formula(A = P(1 + r/100)^t)
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")