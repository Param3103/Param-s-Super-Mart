from stock_management import stock_management
from seller_management import seller_management

task = int(input("Hello Param, what will you like to do today?\nEnter 1 if you would like to add new type of items to your store.\
             \nEnter 2 if you would like to replenish existing stock.\nEnter 3 if you would like to add new vendors to your list."))
if task == 1:
    print("Adding new type of item to store.")
    stock_type = input("What type of item are you adding to the store? ")
    stock_management.adding_new_type(str(stock_type))
elif task == 2:
    print("Replenishing existing stock. ")
    stock_name = input("What item are you replenishing? ")
    qty = int(input("How many of these items are you adding? "))
    stock_management.replenishing_stock(stock_name, qty)
elif task == 3:
    print("Adding new vendors.")
    name = input("What is the name of this vendor? ")
    phone = input("What is his phone number? ")
    email = input("What is his email id? ")
    address = input("What is his address? ")
    seller_management.add_new_seller(name, phone, email, address)