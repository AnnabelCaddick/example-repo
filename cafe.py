menu_items = [('Pizza'), ('Burger'), ('Chips'),('Pasta'), ('Salad')]
i=0


stock = {"Pizza": 10,
              "Burger": 15,
              "Chips": 30,
              "Pasta": 12,
              "Salad": 10
              }


price = {"Pizza": 12,
              "Burger": 15,
              "Chips": 3.50,
              "Pasta": 11,
              "Salad": 10.50
              }
print("### The value of the current stock by item ####")
worth = {item:stock[item]* price[item] for item in menu_items}
for item, value in worth.items():
     print(f"{item}: £{value:.2f}")

total_worth = 0
for value in worth.values():
    total_worth += value 
print (f"The total worth of the current stock: £{total_worth}")