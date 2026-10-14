weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").lower()

## Now, that we got the input from the user  -- weight --  
# we should convert it to its alternative way(menaing either kg or lb).
#  Thus if the entered weight was in kg we multiply it by 2.205
#  and if it was lb then divide by 2.205
if unit == "k":
    lb_weight = weight * 2.205
    print(f"Your LB weight is: {lb_weight:.1f}")
elif unit == "l":
    kg_weight = weight / 2.205
    print(f"Your Kg weight is: {kg_weight:.1f}")
else:
    print("Please write a valid input type")
