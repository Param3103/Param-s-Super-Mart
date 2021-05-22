from customer_management import Customer
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="param_super_mart"
)

my_cursor = my_db.cursor()



print("Welcome to Param's Super mart!")

new = input("Hi, Have you visited us before? Input Y for yes and N for no. ")
while new not in ["Y","N"]:
    new = input("Error! Input Y if you have visited us before and N if you have not. ")
if new == "N":
    print("We would like to know your details so we can customise your experience with our shop to you choices. ")
    name = input("please input your Name. ")
    phone = input("please input your Phone. ")
    email = input("please input your Email. ")
    address = input("please input your Address. ")
    Customer.add_new_customer(Customer(name, phone, email, address))
else:
    name = input("What is your name? ")
    command = "select customer_id, name, phone, email, address from customer_details where name={};".format(name)
    my_cursor.execute(command)
    values = my_cursor.fetchall()
    customer_id = values[0]
    print(values[1:4])
    update = input("Do you want to update your details? Input Y for yes and N for no. ")
    while update not in ["Y", "N"]:
        update = input("Error! Input Y if you want to update your details and N if you don't ")
    if update == "N":
        pass
    else:
        num_identifying_keys = int(input('How many details do you have to identify the contact you need to update? '))
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
        Customer.update_existing_contact(None, identifying_keys, identifying_values, tbc_keys, new_values)
command = "select stock_type from stock_type;"
my_cursor.execute(command)
stock = my_cursor.fetchall()
print("Here is what we have at our store. ")
for s in stock:
    print(s)
continue_buying = True
basket = []
basket_stock_id = []
basket_qty = []
cost = 0
while continue_buying:
    item_type_bought = input("What kind of item do you want to buy? ")
    command = "select type_id from stock_type where stock_type={0}".format(item_type_bought)
    my_cursor.execute(command)
    type_id = my_cursor.fetchall()[0]
    if item_type_bought in stock:
        command = "select stock_name, quantity, sale_price from stock_details where type_id={0};".format(type_id)
        my_cursor.execute(command)
        items = my_cursor.fetchall()
        if len(items) == 0:
            print("Sorry! This kind of item is currently unavailable! ")
            print("Please come again later! ")
        else:
            for item in items:
                if item[3] == 0:
                    items.remove(item)
                else:
                    continue
        if len(items) == 0:
            print("Sorry! This kind of item is currently unavailable! ")
            print("Please come again later! ")
        else:
            print(items)
            item = input("Which item do you want to buy? ")
            while item not in items:
                item = input("Please choose item from above list. ")
                qty = int(input("How many of these do you want to buy? "))
            basket.append(item)
            basket_qty.append(qty)
            my_cursor.execute("select stock_id from stock_details where stock_name=/'{0}/';".format(item))
            stock_id = my_cursor.fetchall()[0]
            basket_stock_id.append(stock_id)
            price = "select sale_price from stock_details where stock_name = {0};".format(item)
            cost += price * qty

    else:
        print(" sorry, we don't offer this item in our store! ")
    Customer.sell_item_to_customer(None, customer_id, basket_stock_id, qty)
    con = input("Do you want to continue buying?Input Y if yes and N if no.")
    if con == "Y":
        continue_buying = True
    elif con == "N":
       continue_buying = False

print(basket)
print("You have to pay $" + cost)
