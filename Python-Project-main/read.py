def read_products(file_path):
     """
     Summary:
        Reads product data from the specified file and organizes it into a dictionary.

     Parameters:
        file_path (str): The path to the text file containing product data.

     Returns:
        tuple: A dictionary of products and the total count of products.

     Raises:
        None
     """
     print('*'*75) #Print table header
     print("Id\tProductName\t Brand\t \tQuantity\tPrice\tOrigin\t")
     print('*'*75)
     
     #open the file and read its content
     file=open(file_path,'r')
     my_items=file.read()
     file.close()
     my_products_in_list=my_items.split('\n')

     while '' in my_products_in_list:
          my_products_in_list.remove('')

     # Counts the number of products(5) in the file   
     counting_the_products = len(my_products_in_list)
     
     # Create a dictionary with product details split into lists
     products_dict = {}
     for i in range(1, counting_the_products + 1):
          products_dict[i] = my_products_in_list[i - 1].split(',')
     return products_dict, counting_the_products

def display_products_table(products_dict):
     """
     Summary:
        Displays the product list in a tabular format with updated prices.

     Parameters:
        products_dict (dict): Dictionary with product details.
     Returns:
        None

     Raises:
        None
     """
     for key, value in products_dict.items():
          print(key, end='\t')
          for i in range(len(value)):
               if i == 3:  # Special handling for price field
                    price = int((int(value[i]) * 200) / 100)

                    products_dict[key][3] = str(price)

                    print('\t', value[i], end='\t')
               elif i == 1:  # Product name field
                    print(value[i], end='\t')
               elif i == 2:  # Brand field
                    print(value[i], end='\t')
               else:
                    print(value[i], end='\t')
          print()
