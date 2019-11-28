# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# BBarth,11.26.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

lstOfProductObjects = []  # List of products


class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        ReadInventoryFromFile(file_name, list_of_objProducts):
        WriteInventoryToFile(file_name): -> (a list of product objects)
    """
    @staticmethod
    def ReadInventoryFromFile(file_name, list_of_objProducts):
        """
        Desc - Reads data from a text file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_objProducts: (list) of tasks in data table, populated by rows in file
        :return (list) of tasks in data table
        """
        try:
            file = open(file_name, "r+")
            for line in file: # use for loop to append each row found in indicated text file to inventory list
                data = line.split(",")
                row = {"product": data[0].strip(), "price": data[1].strip(), "count": data[2].strip()}
                list_of_objProducts.append(row)
            file.close()
            return list_of_objProducts
        except FileNotFoundError as e:  # file not found error handling
            print("Unable to locate the indicated file name!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:  # generic error handling
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def WriteInventoryToFile(file_name, list_of_objProducts):
        """
        Desc - Writes data from a list of dictionary rows into a text file using w+ mode

        :param list_of_objProducts: (list) containing dictionary rows:
        :param file_name: (string) with name of file:
        :return nothing
        """
        try:
            file = open(file_name, "w+")
            for row in list_of_objProducts:  # use for loop to append each row found in table list to indicated text file
                file.write(row["product"] + "," + row["price"] + "," + row["count"] + "\n")
            file.close()
        except FileNotFoundError as e:  # file not found error handling
            print("Unable to locate the indicated file name!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:  # generic error handling
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')

class IO:  # includes functions for add, remove and display of inventory and product data, as well as capturing user
    # operation choice
    """Processes data to and from a file and a list of product objects:
        methods:
            OutputMenuItems(): -> Outputs a list of operations for selection by user
            InputMenuChoice(): -> Determines choice of operation by user
            ShowCurrentProducts(list_of_objProducts): -> Displays current inventory to user
            AddNewProductToInventory(product, price, count, list_of_objProducts): -> Adds new product to inventory
            RemoveProductFromInventory(product, list_of_objProducts): -> Removes a product from inventory
    """
    @staticmethod
    def OutputMenuItems():
        """
        Desc - Display a menu of choices to the user

        :return: nothing
        """
        print('''
            ### Product List - Menu of Operations ###
            1) Load Inventory from File
            2) Review Current Inventory
            3) Add Product to Inventory
            4) Remove Product from Inventory
            5) Save Products to Inventory 
            6) Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """
        Desc - Gets the menu choice from a user

        :return: (string) user choice
        """
        choice = str(input("Which operation would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentProducts(list_of_objProducts):
        """
        Desc - Shows the current products in the data table

        :param list_of_objProducts: (list) of products in data table you want to display
        :return: nothing
        """
        print("******* Current Inventory*******")
        for row in list_of_objProducts:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def AddNewProductToInventory(product, price, count, list_of_objProducts):
        """
        Desc - Adds new product to current inventory

        :param product: (string) identifies name of product to be added to inventory
        :param price: (float) identifies price of product to be added to inventory
        :param count: (float) identifies count of product to be added to inventory
        :param list_of_objProducts: (list) of inventory in data table to which new product will be appended
        :return: (list) of inventory in data table, including new task
        """
        try:
            dicrow = {"product": product, "price": price, "count": count}  # assign product name, price and count
            # values to new dictionary
            list_of_objProducts.append(dicrow)  # append new dictionary to list
            print("Task added successfully!\n")  # confirm addition
            return list_of_objProducts
        except Exception as e:  # generic error handling
            print("Could not add task successfully! There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def RemoveProductFromInventory(product, list_of_objProducts):
        """
        Desc - Removes a product from the data table based on user input

        :param product: (string) identifying the queried product:
        :param list_of_objProducts: (list) containing dictionary rows:
        :return: list of rows in data table, updated following product removal
        """
        try:
            for item in list_of_objProducts:  # iterate over current list. for each item,
                if item["product"].lower() == product.lower():  # if value of task is equivalent to user input
                    list_of_objProducts.remove(item)  # remove the item dictionary from list
                    print("Product successfully removed from inventory...")  # confirm removal
            return list_of_objProducts
        except Exception as e:  # generic error handling
            print("Could not remove successfully! There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')


while True:
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Run ReadInventoryFromFile if "Load Inventory" operation selected
    if strChoice.strip() == '1':
        print("Warning - This action will replace any existing inventory loaded in your session. This will replace "
              "all unsaved changes. Data loss may occur! Recommend to save to file first!")  # Warn user of data loss
        strYesOrNo = input("Reload Inventory without saving? [y/n] - ")  # Double-check with user
        if strYesOrNo.lower() == 'y':
            fileName = input("Identify the .txt file you wish to load data from: ")
            FileProcessor.ReadInventoryFromFile(fileName, lstOfProductObjects)  # read text file data
            IO.ShowCurrentProducts(lstOfProductObjects)  # Show current data in the list/table
        else:
            input("File data was NOT loaded! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Run ShowCurrentProducts function if "Review Current Inventory" operation selected
    if strChoice.strip() == '2':
        IO.ShowCurrentProducts(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Run AddNewProductToInventory function if "Add Product" operation selected
    elif strChoice.strip() == '3':
        strProduct = str(input("What is the product name? ")).strip()  # Get product name from user
        strPrice = str(input("What is the product price? ")).strip()  # Get product price from user
        strCount = str(input("What is the current product count? ")).strip()  # Get product price from user
        IO.AddNewProductToInventory(strProduct, strPrice, strCount, lstOfProductObjects)  # Add product to inventory
        print()  # Add an extra line for looks
        IO.ShowCurrentProducts(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Run RemoveProductFromInventory function if "Remove Product" operation selected
    elif strChoice == '4':
        item_name = str(input("Enter a product to remove: ")).strip()  # Get task from user
        IO.RemoveProductFromInventory(item_name, lstOfProductObjects)  # Remove task from Data table
        print()  # Add an extra line for looks
        continue  # to show the menu

    # Run WriteInventoryToFile function if "Save Products To Inventory" operation selected
    elif strChoice == '5':
        IO.ShowCurrentProducts(lstOfProductObjects)  # Show current inventory
        print()  # Add an extra line for looks
        fileName = input("Identify the .txt file you wish to save current inventory to: ")
        if "y" == str(input("Saving your changes to an existing file will overwrite existing data. Save this data to "
                            "file? ( "
                            "y/n) - ")).strip().lower():  # Double-check with user
            FileProcessor.WriteInventoryToFile(fileName, lstOfProductObjects)  # Save inventory to text file
            input("Data saved to file! Press the [Enter] key to return to menu.")  # Confirm file save
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Break While Loop if "Exit Program" operation selected
    elif strChoice == '6':
        break  # and Exit
