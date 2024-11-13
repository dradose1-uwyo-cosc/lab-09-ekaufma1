# Eleanor
# UWYO COSC 1010
# 11/13/24
# Lab 09
# Lab Section: 15
# Sources, people worked with, help given to:
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria

# You will be creating a Pizza class. It should have the following attributes:
class Pizza: #1st class
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
    def __init__(self, size, sauce='red'):
        self.set_size(size) # - Size
        self.sauce = sauce # - Sauce
        self.toppings = ['cheese'] # - Toppings, which should be a list
# which returns the corresponding attribute, just the value.
    def get_size(self):
        return self.size

    def get_sauce(self):
        return self.sauce

    def get_toppings(self):
        return self.toppings
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
    def set_size(self, size):
        if size >= 10:
            self.size = size
        else:
            self.size = 10
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
    def add_toppings(self, *toppings):
        self.toppings.extend(toppings)
# Create a method that returns the amount of toppings.
    def get_amount_of_toppings(self):
        return len(self.toppings)


# You will be creating a Pizzeria class with the following attributes:
class Pizzeria: #2nd class

# - price_per_topping, a static value for the price per topping of 0.30.
    PRICE_PER_TOPPING = 0.30
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
    PRICE_PER_INCH = 0.60

# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
    def __init__(self):

# - orders, the number of orders placed. Should start at 0.
        self.orders = 0
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
        self.pizzas = []

# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
    def place_order(self):
        
#You will need to prompt the user for:
#     - the size
        size = int(input("Please enter the size of pizza in inches (e.g., 10, 12, 14): "))

#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
        sauce = input("What sauce would you like? Leave blank for red sauce: ")
        if sauce == "":
            sauce = "red"

#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
# I'm doing a while loop
        toppings = []
        while True:
            topping = input("Please enter a topping (or press Enter to finish): ")
            if topping == "":  # Break the loop if input is empty
                break
            toppings.append(topping)

        while topping != "":
            toppings.append(topping)
            topping = input("What other topping would you like? (Enter to finish): ")

#   - Upon completion, create the pizza object and store it in the list.
        
        pizza = Pizza(size, sauce)  # Creates the pizza without toppings initially
        pizza.add_toppings(*toppings)  # Adds toppings
        self.pizzas.append(pizza)
        self.orders += 1

#- getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
    def get_price(self, pizza):
        size_price = pizza.get_size() * self.PRICE_PER_INCH
        toppings_price = pizza.get_amount_of_toppings() * self.PRICE_PER_TOPPING
        return size_price + toppings_price
    
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
    def get_receipt(self, pizza):
        price = self.get_price(pizza)
        receipt = f"""

Pizza Receipt

Sauce: {pizza.get_sauce()}
Size: {pizza.get_size()}
Toppings: {', '.join(pizza.get_toppings())}

Price: ${price:.2f}

"""
        print(receipt)
    
# - getNumberOfOrders()
#   - This will simply return the number of orders.
    def get_number_of_orders(self):
        return self.orders

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
pizzeria = Pizzeria()
while True:
    order_prompt = input("Would you like to place an order? type 'exit' to exit\n")
    if order_prompt.lower() == 'exit':
        break
    pizzeria.place_order()
    pizzeria.get_receipt(pizzeria.pizzas[-1])

print(f"\nTotal number of orders placed: {pizzeria.get_number_of_orders()}")

# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""

