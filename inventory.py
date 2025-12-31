
from tabulate import tabulate

#=======The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        #initialise attributes
  
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
        
    def get_cost(self):
        return self.cost
    

    def get_quantity(self):
        return self.quantity
       

    def __str__(self):
        return f"{self.country} | {self.code} | {self.product} | cost: ${self.cost:.2f} | Quantity: {self.quantity}"
        
        
#=============Shoe list===========

shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():

    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(",")
                if len(data) != 5:
                    continue
                country, code, product, cost, quantity = [item.strip() for item in data]
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt not found.")
    except Exception as e:
        print (f"Error reading file: {e}")


def capture_shoes():
    country = input(" Enter country: ")
    code = input("Enter product code: ")
    product = input("Enter product name: ")
    cost = input("Enter product cost: ")
    quantity = input("Enter quantity: ")

    try:
        cost = float(cost)
        quantity = int(quantity)
    except ValueError:
        print("Cost must be a number and quantity must be an integer.")
        return

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    update_inventory_file()

    with open("inventory.txt" , "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

def view_all():
    if not shoe_list:
        print("No shoes available.")
        return

    table = []
    headers = ["Country", "Code", "Product", "Cost" , "Quantity"]

    for shoe in shoe_list:
        table.append([
            shoe.country,
            shoe.code,
            shoe.product,
            f"{shoe.cost:.2f}",
            shoe.quantity
        ])
    
    
    print(tabulate(table, headers=headers, tablefmt="grid"))


def re_stock():
    if not shoe_list:
        print("No shoes available.")
        return
    
    lowest_shoe = min(shoe_list, key=lambda s: s.quantity)
    print("Shoe with lowest quantity: ")
    print(lowest_shoe)

    choice = input("Would you like to add stock? (yes/no): ").lower()
    if choice == "yes":
        try:
            add_qty = int(input("Enter quantity to add:"))
            if add_qty <= 0:
                print("Quantity must be positive.")
                return
            lowest_shoe.quantity += add_qty
            update_inventory_file()
            print("Stock updated successfully.")
        except ValueError:
            print("Invalid quantity entered.")
   

def search_shoe():
    """Search for a shoe using its code"""
    code = input("Enter shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            table = [[shoe.country, shoe.code, shoe.product, f"{shoe.cost:.2f}", shoe.quantity]]
            headers = ["Country", "Code", "Product", "Cost", "Quantity"]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            return
    print("Shoe not found.")

def value_per_item():
    """Calculate and display value per item"""
    table = []
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        table.append([
            shoe.product,
            f"{shoe.cost:.2f}",
            shoe.quantity,
            f"{value:.2f}"
        ])
    headers = ["Product", "Cost", "Quantity", "Total Value"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def highest_qty():
    """Display the shoe with the highest quantity"""
    if not shoe_list:
        print("No shoes available.")
        return
    

    highest_shoe = max(shoe_list, key=lambda s: s.quantity)
    table = [[
        highest_shoe.country,
        highest_shoe.code,
        highest_shoe.product,
        f"{highest_shoe.cost:.2f}",
        highest_shoe.quantity
    ]]

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print("Shoe with highest quantity for sale: ")
    print(tabulate(table, headers=headers, tablefmt="grid"))
#==========Main Menu=============

def update_inventory_file():
    """Rewrite inventory.txt with updated data"""
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
            )


def main_menu():
    read_shoes_data()

    while True:
        print("\n===== Shoe Inventory Menu =====")
        print("1. View all shoes")
        print("2. Capture new shoe")
        print("3. Restock lowest quantity shoe")
        print("4. Search for a shoe")
        print("5. Value per item")
        print("6. Highest quantity shoe")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice =="5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid choice! Please make your choice again.")


if __name__ == "__main__":
    main_menu()







