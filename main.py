#Importing necessary functions from the modules
from read import read_products, display_products_table
from operation import process_purchase, print_customer_invoice, print_supplier_invoice, process_restock
from write import write_customer_invoice, update_products_file, write_supplier_invoice

def display_menu():
    """
    Summary:
        Displays the main menu of the WeCare Store System.

        This function outputs a list of options for the user to interact with the system.
        It includes functionalities such as displaying products, making purchases,
        generating invoices, restocking items, and exiting the system.

    Parameters:
        None

    Returns:
        None

    Raises:
        None
    """
    print("\n"+"="*50)
    print("\t\tWeCare Store System")
    print("="*50)
    print("1. Display Products")
    print("2. Make a Purchase")
    print("3. Generate Customer Invoice")
    print("4. Restock Products")
    print("5. Exit")
    print("="*50)

def main():
    """
    Summary:
    Main function for the WeCare Store System.

    This function serves as the entry point for the inventory and invoice management system.
    It displays a menu to the user and handles different operations based on user input,
    including displaying products, processing purchases, generating customer invoices,
    restocking inventory, and exiting the application.

    Functionalities:
    - Reads product data from a file.
    - Displays available products.
    - Allows customers to make purchases and generates their invoice.
    - Allows suppliers to restock inventory and generates restock invoice.
    - Updates the product file with new inventory data.
    Parameters:
        None

    Returns:
        None

    Raises:
        ValueError: If the user inputs a non-integer value when prompted for menu choice.
    """

    #Path to the product data file    
    file_path='Text File/WeCare Store.txt'
    products_dict=None
    counting_the_products=0
    user_products= []
    quantity_products= []
    total= 0
    vat= 0
    grand_total= 0
    total_free_items= 0
    user_name= ""
    user_address= ""

    '''Infinite loop to keep the program running until
    the user chooses to exit.'''
    while True:
        display_menu() #show main menu
        try:
            choice=int(input("Enter your choice(1-5):"))

            # Option 1: Display available products
            if choice==1:
                products_dict, counting_the_products=read_products(file_path)
                display_products_table(products_dict)

            # Option 2: Process purchase
            elif choice==2:
                if products_dict is None:
                    products_dict, counting_the_products=read_products(file_path)

                #Handle customer purchases
                user_products, quantity_products, total, total_free_items=process_purchase(products_dict, counting_the_products)
                user_name=input("Enter your name: ")
                user_address=input("Enter your address: ")

                # Update product data file after purchase
                update_products_file(file_path, products_dict)

            # Option 3: Generate customer invoice
            elif choice==3:
                if not user_products:
                    print("No purchase made yet. Please make a purchase first.")
                else:
                    print_customer_invoice(user_name, user_address, user_products, quantity_products, total, total_free_items)
                    write_customer_invoice(user_name, user_address, user_products, quantity_products, total, total_free_items)

            # Option 4: Restock products
            elif choice==4:
                if products_dict is None:
                    products_dict, counting_the_products=read_products(file_path)
                 # Process restocking operation
                supplier_name, restock_items, subtotal, vat, grand_total= process_restock(products_dict)

                if restock_items:
                    # Write supplier invoice and update products file
                    write_supplier_invoice(supplier_name, restock_items, subtotal,vat, grand_total)
                    update_products_file(file_path, products_dict)
                print("\nRestock completed and products updated!")

            # Option 5: Exit the program
            elif choice==5:
                print("Thankyou for using our application")
                break

            else:
                print("Invalid choice! Please enter a number between 1 to 5.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Call main to start the program
main()
    

                
