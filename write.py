import datetime

def write_customer_invoice(user_name, user_address, user_products, quantity_products, total , total_free_items):
     """
     Summary:
     Generates and writes a customer's invoice to a text file named after the customer.

     Parameters:
     user_name (str): The name of the customer (used as the filename).
     user_address (str): The address of the customer.
     user_products (list): A list of product names purchased by the customer.
     quantity_products (list): A list of quantities corresponding to the products purchased.
     total (int): The total cost of the purchase.
     total_free_items (int): The number of free items received as part of the offer.

     Returns:
          None

     Raises:
          None

     Examples:
          write_customer_invoice("Alice", "Kathmandu", ["Soap", "Shampoo"], [2, 1], 300, 1)
     """
     #Get the current date
     date_time = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)

     #Open a file using the customer name to save the invoice
     w=open(user_name,"w")
     w.write('-'*75)
     w.write('\n')
     w.write("\t\t\t Invoice(We Care)")
     w.write('\n')
     w.write("Customer Name: "+user_name)
     w.write('\t\t\t\t')
     w.write("Date: "+date_time)
     w.write('\n')
     w.write('Address: '+user_address)
     w.write('\n')
     w.write('-'*75)
     w.write('\n')
     w.write("Product Name\t\tQuantity")
     w.write('\n')

     '''
     Loop through each purchased product and write the name and quantity
     to the file.
     '''
     for i in range(len(user_products)):
          product = user_products[i]
          quantity = str(quantity_products[i])
          w.write(product + "\t\t" + quantity+"\n")
     w.write('-'*75)
     w.write('\n')
     w.write("Total: "+str(total))
     w.write('\n')
     w.write('-'*75)
     if total_free_items!=0:
          w.write('\n')
          w.write("\t\t*****you have got "+str(total_free_items)+" free products*****")
          w.write('\n')
          w.write('-'*75)

     w.close()

def write_supplier_invoice(supplier_name, restock_items, subtotal, vat,grand_total):
     """
     Summary:
     Generates and writes a supplier restocking invoice to a text file named with the current date.

     Parameters:
     supplier_name (str): Name of the supplier.
     restock_items (list of dict): A list where each dictionary represents a restocked item,
     containing 'product', 'brand', 'quantity', 'rate', and 'total'.
     subtotal (float): The subtotal amount of the restocked items.
     vat (float): The calculated VAT (typically 13% of subtotal).
     grand_total (float): The total amount after including VAT.

     Returns:
          None

     Raises:
          None

     Example:
     restock_items = [
     {'product': 'Soap', 'brand': 'Lux', 'quantity': 50, 'rate': 30, 'total': 1500},
     {'product': 'Shampoo', 'brand': 'Head & Shoulders', 'quantity': 20, 'rate': 120, 'total': 2400}
     ]
     write_supplier_invoice("ABC Suppliers", restock_items, 3900, 507, 4407)
     """
     date_time = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)

     invoice_name = "Restock_" +" "+ date_time + ".txt"

     w=open(invoice_name, "w")
     w.write('-'*75)
     w.write('\n')
     w.write("\t\t\t Supplier Restock Invoice")
     w.write('\n')
     w.write('-'*75)
     w.write('\n')
     w.write("Supplier Name: "+supplier_name)
     w.write('\t\t\t\t')
     w.write("Date:" +date_time)
     w.write('\n')
     w.write('-'*75)
     w.write('\n')
     w.write("Product Name\t\t Brand\t\tQuantity\tRate\tTotal")
     w.write('\n')
     
     '''
     Write details of each restocked item including product name, brand,
     quantity, rate, and total cost.
     '''
     for item in restock_items:
          line=item['product'] + "\t\t"+item['brand']+"\t"+str(item['quantity'])+"\t\t"+str(item['rate'])+"\t"+str(item['total'])
          w.write(line+'\n')

          w.write('-'*75)
          w.write('\n')
          w.write("Subtotal: "+str(subtotal))
          w.write('\n')
          w.write("VAT (13%): "+str(vat))
          w.write('\n')
          w.write("Grand Total: "+str(grand_total))
          w.write('\n')
          w.write('-'*75)
          w.close()
def update_products_file(file_path,products_dict):
     """
     Summary:
     Updates the product file with the latest data from the products dictionary.

     Parameters:
     file_path (str): Path to the product file to be updated.
     products_dict (dict): Dictionary where each key is a product ID and each value is a list of product attributes.

     Returns:
          None

     Raises:
          None
     """
     file=open(file_path,'w')

     '''
     Loop through each product and write its attributes to the file
     in comma-separated format.
     '''
     for key, value in products_dict.items():
          line=','.join(value)+'\n'
          file.write(line)
     file.close()
