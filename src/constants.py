new = input("Hi, Have you visited us before? Input Y for yes and N for no. ")
name = input("please input your Name. ")
phone = input("please input your Phone. ")
email = input("please input your Email. ")
address = input("please input your Address. ")
update = input("Do you want to update your details? Input Y for yes and N for no. ")
num_identifying_keys = int(input('How many details do you have to identify the contact you need to update? '))
identifying_key = input(
    'what kind of detail do you have? \nName, Phone, EmailID or Address. Plz input in same form.')
identifying_value = input('Plz input the contact detail now. ')
num_tbc_keys = int(input('How many details of this contact do you want to change? '))
tbc_key = input(
                'what kind of detail do you want to change? \nName, Phone, EmailID or Address. Plz input in same form.')

new_value = input('Plz input the new contact detail now. ')
item_type_bought = input("What kind of item do you want to buy? ")
con = input("Do you want to continue buying?Input Y if yes and N if no.")
task = int(input("Hello Param, what will you like to do today?\nEnter 1 if you would like to add new type of items to your store.\
             \nEnter 2 if you would like to replenish existing stock.\nEnter 3 if you would like to add new vendors to your list.\
                 \nEnter 4 if you would like to update details of your vendor.\nEnter 5 if you want to add new stock of items. \n\
                 Enter 6 if you want to find stock."))
stock_type = input("What type of item are you adding to the store? ")
stock_name = input("What item are you replenishing? ")
qty = int(input("How many of these items are you adding? "))
type = input("Which kind of stock are you adding? ")
stock_name = input("What is the name of this " + type + "? ")
quantity = int(input("How many of {0} do you need? ".format(stock_name)))
price_when_bought = float(input("How much did you buy it for? "))
seller = input("Who did you buy it from? ")
price_for_customers = float(input("How much are you selling it for? "))
qty = input("How many types of information do you have abt this item? ")
key = input("Do you have the name, type or seller of this item? ")
value = input("What is the {0} of the item? ".format(key))