import datetime
def print_customer_invoice(user_name, user_address, user_products, quantity_products, total, total_free_items):
    """
    Summary:
        Prints the invoice for a customer purchase with date and totals.

    Parameters:
        user_name (str): Customer name.
        user_address (str): Customer address.
        user_products (list): List of product names.
        quantity_products (list): List of product quantities.
        total (int): Total cost.
        total_free_items (int): Number of bonus free items.
    Returns:
        None

    Raises:
        None
    """
    # Get current date in YYYY-MM-DD format
    date_time=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day)

    print('-'*75)
    print("\t\t\t Invoice(We Care)")
    print('-'*75)
    print("Customer name:",user_name, end="\t")
    print("\t\t\t\t Date:"+date_time, end="\n")
    print("Address:", user_address)
    print('-'*75)
    print("Product Name\t\tQuantity")

    '''
    Loop through all purchased products and print their names and corresponding quantities.
    This section generates the detailed list of what the customer has bought.
    '''
    for i in range(len(user_products)):
        product = user_products[i]
        quantity = str(quantity_products[i])
        print(product + "\t\t" + quantity)

    print('-'*75)
    print("Total: ",total,end="\n")
    print('-'*75)

    '''
    If the customer received any free bonus items as part of the deal
    (e.g., 1 free for every 3 bought), it will be shown here.
    '''
    if total_free_items!=0:
        print("\t\t *****you have got ",total_free_items,"free products*****")
        print('-'*75)

def process_purchase(products_dict, counting_the_products):
    """
    Summary:
        Handles the customer purchasing process, calculates totals and updates stock.

    Parameters:
        products_dict (dict): Product details with stock info.
        counting_the_products (int): Total number of products.

    Returns:
        tuple: Lists of purchased items, quantities, total cost, and number of free items.

    Raises:
        ValueError: If non-numeric input is entered for product ID or quantity.
    """
    user_products=[]
    quantity_products=[]
    total=0
    total_free_items=0
    purchased_quantity={}

    '''
    This loop allows the user to continue buying multiple items until they choose to stop.
    It validates input, checks stock, handles free items, and updates stock levels.
    '''
    continue_=True
    while continue_==True:
        try:
            user_buy=int(input("Enter the product id: "))
            if user_buy < 1 or user_buy > counting_the_products:
                print("\nInvalid product ID! Please enter a Id between 1 and", counting_the_products)
                continue
            if user_buy<=counting_the_products and user_buy!=0:
                quantity=int(input("Enter the product quantity: "))

                if quantity<= int(products_dict[user_buy][2]):
                    user_products.append(products_dict[user_buy][0])
                    free=quantity//3
                    total_quantity=quantity+free

                    current_price=int(products_dict[user_buy][3])

                    if total_quantity> int(products_dict[user_buy][2]):
                        products_dict[user_buy][2]=str(int(products_dict[user_buy][2])-quantity)
                        total+=(quantity*current_price)
                        quantity_products.append(quantity)
                    else:
                        total+=(quantity*current_price)
                        quantity_products.append(total_quantity)
                        products_dict[user_buy][2]=str(int(products_dict[user_buy][2])-total_quantity)
                else:
                    print("The available stock for product is: ",products_dict[user_buy][2])
                    continue
                total_free_items+=free
                ask=input("Will you like to buy more items(yes/no): ")
                if ask.lower()=='no':
                    break
        except ValueError:
            print("Invalid input!Please enter a numeric value")
            continue

    return user_products, quantity_products, total, total_free_items

def print_supplier_invoice(supplier_name, restock_items, subtotal, vat, grand_total):
    """
    Summary:
    Prints a formatted supplier restock invoice to the console.

    This function displays a restocking invoice containing the supplier's name,
    current date, and a detailed list of restocked items including their brand, 
    quantity, rate, and total price. It also shows the subtotal, VAT, and grand total.

    Parameters:
        supplier_name (str): The name of the supplier providing the restock.
        restock_items (list of dict): A list where each dictionary contains product
            information with keys 'product', 'brand', 'quantity', 'rate', and 'total'.
        subtotal (float): The total price before tax.
        vat (float): The value-added tax amount (typically 13% of subtotal).
        grand_total (float): The total amount payable including VAT.

    Returns:
        None

    Raises:
        None
    """
    date_time=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day)

    print('-'*75)
    print("\t\t\t Supplier Restock Invoice")
    print('-'*75)
    print("Supplier Name: "+supplier_name+"\t\t\t\tDate: "+date_time)
    print('-'*75)
    print("Product Name\t\t Brand\t\tQuantity\tRate\tTotal")

    for item in restock_items:
        product_line=item['product']+"\t\t"+item['brand']+"\t"+str(item['quantity'])+"\t\t"+str(item['rate'])+"\t"+str(item['total'])
        print(product_line)

    print('-'*75)
    print("Subtotal: "+str(subtotal))
    print("Vat (13%): "+str(vat))
    print("Grand Total: "+str(grand_total))
    print('-'*75)
    
def process_restock(products_dict):
    """
    Summary:
        Allows supplier to restock products and calculates the restock invoice.

    Parameters:
        products_dict (dict): Product details with stock info.

    Returns:
        tuple: Supplier name, restocked items, subtotal, VAT, and grand total.

    Raises:
        ValueError: If quantity or cost input is invalid.
    """
    restock_items=[]
    subtotal=0
    supplier_name=input("Enter supplier name:")

    '''
    This loop allows the supplier to restock multiple products.
    It keeps adding restock details until the user exits by entering product_id = 0.
    '''
    while True:
        print("\nCurrent Products")
        for key,value in products_dict.items():
            print(key,"-",value[0],"Current stock:", value[2]+")")
        try:
            product_id=int(input("\nEnter product ID(1-5) to restock and 0 to exit:"))
            if product_id==0:
                break
            if product_id not in products_dict:
                print("Invalid product ID! Please try again.")
                continue

            quantity=int(input("Enter quantity to add:"))
            rate=int(input("Enter cost per unit: "))

            item_total= quantity*rate
            
            # Append new restock item to list
            restock_items.append({
                'product':products_dict[product_id][0],
                'brand':products_dict[product_id][1],
                'quantity':quantity,
                'rate':rate,
                'total': item_total
                })
            #Update stock in dictionary
            products_dict[product_id][2]=str(int(products_dict[product_id][2])+quantity)
            subtotal+=item_total

        except ValueError:
            print("Invalid input! Please enter the number.")

    vat=subtotal*0.13
    grand_total=subtotal+vat
    print_supplier_invoice(supplier_name, restock_items, subtotal, vat, grand_total)
    return supplier_name,restock_items,subtotal,vat,grand_total
            
