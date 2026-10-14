#Defining the menu using dictionaries(key being product and value being the price)
menu = {"pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}
#for now, empty cart and 0 total
cart = []
total = 0
#showcasing the menu. (key:10) reserves some space so that prices line up perfectly(for better UX) 
print("----MENU---")
for key, value in menu.items():
    print(f"{key:10}: ${value}")
print("-------")

#in while loop asking for the user to enter what products to buy unless they choose to quit
while True:
    food = input("Select an item(q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
#showing their order, while also calculating total
print("----YOUR ORDER----")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: ${total:.2f}") #showing total 