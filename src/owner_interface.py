from stock_management import stock_management
from seller_management import seller_management
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="param_super_mart"
)

mycursor = mydb.cursor()

task = int(input("Hello Param, what will you like to do today?\nEnter 1 if you would like to add new type of items to your store.\
             \nEnter 2 if you would like to replenish existing stock.\nEnter 3 if you would like to add new vendors to your list.\
                 \nEnter 4 if you would like to undate details of your vendor.\nEnter 5 if you want to add new stock of items."))
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
elif task == 4:
    print("Updating details of vendors.")
    num_identifying_keys = int(input('How many details do you have to identify the vendor whose details you need to update? '))
    identifying_keys = []
    identifying_values = []
    for num in range(num_identifying_keys):
        identifying_key = input(
            'what kind of detail do you have? \nName, Phone, EmailID or Address. Plz input in same form.')
        identifying_keys.append(identifying_key)
        identifying_value = input('Plz input the contact detail now. ')
        identifying_values.append(identifying_value)
    num_tbc_keys = int(input('How many details of this contact do you want to change? '))
    tbc_keys = []
    new_values = []
    for num in range(num_tbc_keys):
        tbc_key = input(
            'what kind of detail do you want to change? \nName, Phone, EmailID or Address. Plz input in same form.')
        tbc_keys.append(tbc_key)
        new_value = input('Plz input the new contact detail now. ')
        new_values.append(new_value)
    seller_management.update_seller_contact(identifying_keys, identifying_values, tbc_keys, new_values)
elif task == 5:
    type = input("Which kind of stock are you adding? ")
    stock_name = input("What is the name of this " + type + "? ")
    quantity = int(input("How many of {0} do you have right now? ").format(stock_name))
    price_when_bought = float(input("How much did you buy it for? "))
    seller = input("Who did you buy it from? ")
    mycursor.execute("select seller_id from seller_details where name='{0}'".format(seller))
    seller_id = mycursor.fetchall()[0]
    price_for_customers = float(input("How much are you selling it for? "))
    stock_management.adding_new_stock(stock_name, type, quantity, price_when_bought, seller_id, price_for_customers)