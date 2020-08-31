# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (D, Completed assignment, 2020-08-31):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <D>,<2020-08-31>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt' # The name of the data file
product_objects = [] # List of product objects
name = ""  # Used for product name
price = ""  # used for product price

class Product(object):
    """Stores data about a product """

    # Creates constructor
    def __init__(self, name, price):
        self.product_name = str(name)
        self.product_price = float(price)

    # Overrides the default __str__() method to provide product name and price
    def __str__(self):
        return self.product_name + ", " + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name): # Loads products.txt
        product_objects.clear()
        file = open(file_name, "r")
        for line in file:
            name, price = line.split(",")
            product = Product(name, format(float(price), ".2f"))
            product_objects.append(product)
        file.close()
        return product_objects

    @staticmethod # Processes data to the file.
    def save_data_to_file(file_name, product_objects):
        file = open(file_name, "w")
        for product in product_objects:
            file.write(str(product) + "\n")
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod # Display menu to user
    def display_menu():
        print('''
        Menu of Options
        1) Display Products
        2) Add Products
        3) Save and Exit
        ''')
        print()

    @staticmethod # Get input from user from menu
    def user_menu_choice():
        choice = str(input("Which option? [1 to 3] - ")).strip()
        print()
        return choice

    @staticmethod # Displays current list of products
    def show_current_data(list_of_products):
        print("******* The current products are: ********")
        for row in list_of_products:
            print(row)
        print("******************************************")

    @staticmethod # Get input from user for new product and price
    def user_product_input():
        product_name = input("Enter a product name: ").strip()
        product_price = format(float(input("Enter a product price: ")), ".2f")
        product = Product(product_name, product_price)
        return product

    @staticmethod  # Function that causes program to pause before continuing.
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to exit program.')

    @staticmethod  # Function that gets a yes or no from the user.
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - Load existing data
product_objects = FileProcessor.read_data_from_file(file_name)

while(True):
    # Step 2 - Show user menu
    IO.display_menu()

    # Step 3 - Process user's menu choice
    choice = IO.user_menu_choice()

    if choice == '1': # Show current data
        IO.show_current_data(product_objects)

    elif choice == '2': # Add new data
        product = IO.user_product_input()
        product_objects.append(product)

    elif choice == '3': # Save and Exit
        choice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if choice.lower() == "y":
            FileProcessor.save_data_to_file(file_name, product_objects)
            IO.input_press_to_continue("Save Succeeded!")
            break
        else:
            print("Save Cancelled!")
            continue
# Main Body of Script  ---------------------------------------------------- #