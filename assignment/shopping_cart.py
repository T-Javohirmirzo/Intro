foods = []
prices = []
total = 0
# A while loop that continuously prompts the user to add items until they enter 'q' to quit
while True:
    food = input("Enter food to buy(q to quit): ")
    if(food=="q"):
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food, price in zip(foods, prices): ## I used zip method, which is not in the video, so that the user can see the price of each item bought along with its name. This creates a better UX for the program
    print(f"{food}: {price}")
# Sum up all individual prices to calculate the final total
for price in prices:
    total += price

print()
print(f"Your total is: {total}")